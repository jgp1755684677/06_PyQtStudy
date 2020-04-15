# -*- coding: utf-8 -*-
import fiona
import numpy as np
import matplotlib.pyplot as plt
import os
import rasterio
import rasterio.mask
from rasterio.plot import show, show_hist
from rasterio.warp import calculate_default_transform, reproject
from rasterio import crs
from rasterio.enums import Resampling


# get tiff information
def get_tiff_info(filename):
    # open tiff
    with rasterio.open(filename) as ds:
        # export datatype
        print(f'数据格式：{ds.driver}')
        # export band counts
        print(f'波段数目：{ds.count}')
        # export image width
        print(f'影像宽度：{ds.width}')
        # export image height
        print(f'影像高度：{ds.height}')
        # export image boundary
        print(f'地理范围：{ds.bounds}')
        # export reflection transformation parameter
        print(f'反射变换参数（六参数模型）：\n {ds.transform}')
        # export projection
        print(f'投影定义：{ds.crs}')
        # show the histogram
        show_hist(ds, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title='Histogram')
        # get the bands counts
        num_bands = ds.count
        # show the image
        for index in range(num_bands):
            # define band number.
            band = index + 1
            # show the gray image.
            show((ds, band), title="band" + str(band), cmap='Greys_r')
            # show the histogram of every band.
            plt.hist(ds.read(band))
            # show the title of every band.
            plt.title("band" + str(band) + " histogram")
            # show.
            plt.show()


# show the image and histogram.
def show_tiff(filename):
    # open data source.
    with rasterio.open(filename) as ds:
        # show the data source.
        show(ds)
        # show the histogram.
        show_hist(ds, bins=50, lw=0.0, stacked=False, alpha=0.3, histtype='stepfilled', title="Histogram")


# get image band.
def get_band(filename, bandID):
    # open the data source.
    with rasterio.open(filename) as ds:
        # judge if the bandID exists.
        if bandID in len(ds.count):
            # read the band which band number is bandID.
            band = ds.read(bandID)
    # return the band.
    return band


# raster resampling.
def tiff_resample(filename, scale):
    # scale = 2
    # Down sampling to 1/2 of the resolution can be done with scale = 1/2.
    # open the image needed to resample.
    with rasterio.open(filename) as dataset:
        # get the data
        data = dataset.read(
            out_shape=(dataset.count, int(dataset.height * scale), int(dataset.width * scale)),
            resampling=Resampling.cubic)

        # scale image transform
        out_transform = dataset.transform * dataset.transform.scale(
            (dataset.width / data.shape[-2]),
            (dataset.height / data.shape[-1])
        )
        # assignment
        out_meta = dataset.meta
        # define the information of export image.
        out_meta.update({"driver": "GTiff",
                         "height": data.shape[1],
                         "width": data.shape[2],
                         "transform": out_transform})
    # get filename without suffix.
    filename_prefix = filename.split('.')[0]
    # define the name of export image
    out_filename = filename_prefix + "_resample.tif"
    print('out_TIFF:' + out_filename)
    # 输出裁剪后栅格，w为write，写
    with rasterio.open(out_filename, "w", **out_meta) as dest:
        dest.write(data)  # 输出重采样后的影像数据
    show_tiff(out_filename)


# clip the raster image by ShapeFiles.
def tiff_clip_by_shp(raster_filename, vector_filename):
    # open the ShapeFiles and read it.
    with fiona.open(vector_filename, "r") as shp:
        # get the information of geometry in ShapeFiles.
        shapes = [feature["geometry"] for feature in shp]

    # open the raster needed to clip.
    with rasterio.open(raster_filename) as src:
        # show the original image.
        show_tiff(raster_filename)
        # clip the raster image.
        out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
        # assign the data to export file.
        out_meta = src.meta
        # define the information of export image
        out_meta.update({"driver": "GTiff",
                         "height": out_image.shape[1],
                         "width": out_image.shape[2],
                         "transform": out_transform})
    # get the name of raster image without suffix.
    raster_filename_prefix = raster_filename.split('.')[0]
    # define the name of export image.
    out_raster_filename = raster_filename_prefix + "_clip.tif"
    # export the name of export image.
    print('Export Image Name: ' + out_raster_filename)
    # open the export image.
    with rasterio.open(out_raster_filename, "w", **out_meta) as dest:
        # write data to export image.
        dest.write(out_image)
    # show the clipped image
    show_tiff(out_raster_filename)


# transfer image projection
def transfer_raster_projection(filename_src, epsg_name):
    # define the information of projection which transfer to.
    dst_crs = crs.CRS.from_epsg(epsg_name)
    # open the original image.
    with rasterio.open(filename_src) as src_ds:
        # get the information of the original image.
        profile = src_ds.profile
        # calculate the data.
        dst_transform, dst_width, dst_height = calculate_default_transform(
            src_ds.crs, dst_crs, src_ds.width, src_ds.height, *src_ds.bounds)
        # update the information
        profile.update({
            'crs': dst_crs,
            'transform': dst_transform,
            'width': dst_width,
            'height': dst_height,
            'nodata': 0
        })
        # get filename without suffix
        filename_src_prefix = filename_src.split('.')[0]
        # define the export name.
        out_filename = filename_src_prefix + "_" + epsg_name + ".tif"
        print('Export filename:' + out_filename)
        # open the export image.
        with rasterio.open(out_filename, 'w', **profile) as dst_ds:
            # define the band_ID
            band_ID = src_ds.count + 1
            for i in range(1, band_ID):
                # read every band.
                src_array = src_ds.read(i)
                # get the datatype of band.
                dst_array = np.empty((dst_height, dst_width), dtype=profile['dtype'])
                # project the band.
                reproject(
                    source=src_array,
                    src_crs=src_ds.crs,
                    src_transform=src_ds.transform,
                    destination=dst_array,
                    dst_transform=dst_transform,
                    dst_crs=dst_crs,
                    resampling=Resampling.cubic,
                    num_threads=2)
                # write the data to file.
                dst_ds.write(dst_array, i)
    # show the reproject image.
    show_tiff(out_filename)


# calculate NDVI of image.
def calculate_ndvi(filename):
    # open the image.
    with rasterio.open(filename) as src:
        # show the image.
        show_tiff(filename)
        # red the band3 and band4.
        red = src.read(3)
        nir = src.read(4)
        # get the information of image.
        profile = src.profile
        # get filename without suffix.
        filename_prefix = filename.split('.')[0]
        # define the export filename
        out_filename = filename_prefix + "_NDVI.tif"
        # export the name of export image.
        print('Export filename:' + out_filename)
        # calculate the ndvi.
        with np.errstate(divide='ignore', invalid='ignore'):
            # calculate.
            ndvi = (nir - red) / (nir + red + 0.00001)
            # set the zero.
            ndvi[ndvi == np.inf] = 0
            # add data to array
            ndvi = np.nan_to_num(ndvi)
            # update the information of image.
            profile.update(dtype=ndvi.dtype, count=1)
        # open the export image.
        with rasterio.open(out_filename, mode='w', **profile) as dst:
            # write the date to file.
            dst.write(ndvi, 1)
        # show the image.
        show(ndvi, cmap='Greys_r')


# information extraction
def get_subdata(filename, threshold):
    # open the image.
    with rasterio.open(filename) as src:
        # show the image.
        show_tiff(filename)
        # read the band four.
        nir_band = src.read(4)
        # get the information of the original image.
        profile = src.profile
        # update the information of image.
        profile.update({"driver": "GTiff", "count": 1})
        # get filename without suffix.
        filename_prefix = filename.split('.')[0]
        # define the name of export image.
        out_filename = filename_prefix + "_sub.tif"
        # export the name of export image.
        print('Export filename:' + out_filename)
        # extract the information.
        with np.errstate(divide='ignore', invalid='ignore'):
            # set the value less than threshold to zero.
            subdata = np.where(nir_band <= threshold, 0, nir_band)
            # set the value more than threshold to 1.
            subdata = np.where(subdata > threshold, 1, subdata)
            # export subdata.
            print(subdata)
        # open export image.
        with rasterio.open(out_filename, mode='w', **profile) as dst:
            # write the data to file.
            dst.write(subdata, 1)
        # show the export image.
        show_tiff(out_filename)


if __name__ == '__main__':
    # get path of the project.
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # export project path.
    print("Root path:" + root_path)
    # define the path of data.
    data_path = os.path.abspath(root_path + r"\RasterData")
    # export data path.
    print("Data path:" + data_path)
    # change the path.
    os.chdir(data_path)
    # the file needed to operate.
    tiff_filename = "LC08_L1TP_121036_20180325_20180404_01_T1_clip.tif"
    # the shapefile used to clip raster image.
    shapefile_filename = os.path.abspath(root_path + r"\RasterData\TestClip.shp")
    # call the function.
    # get_tiff_info(tiff_filename)
    # transfer_raster_projection(tiff_filename, "4326")
    # tiff_clip_by_shp(tiff_filename, shapefile_filename)
    # tiff_resample(tiff_filename, 2)
    # calculate_ndvi(tiff_filename)
    test_tiff = "T50RKU_20200320T025541_2348_clip.tif"
    get_subdata(test_tiff, 3000)
