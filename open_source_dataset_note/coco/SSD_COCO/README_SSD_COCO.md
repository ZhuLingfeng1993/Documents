Author: zhulingfeng 

I modify the program in step 4 and 5.

The program in official `CAFFE_SSD/data/coco` is specified to COCO2014-2015 dataset. I use the coco2017 dataset  without test images so I need to modify the dataset name in files in step 4 and 5

### Preparation

1. Download Images and Annotations from [MSCOCO](http://mscoco.org/dataset/#download). 

   assume data is stored in `$COCO_ROOT, and then put images in folder `images/`(e.g. put train2017 images in `images/train2017/`)  and put annotations in folder `annotations/` 

2. Get the coco code. We will call the directory that you cloned coco into `$COCO_ROOT`
  ```Shell
  git clone https://github.com/weiliu89/coco.git
  cd coco
  git checkout dev
  ```

3. Build the coco code.
  ```Shell
  cd PythonAPI
  python setup.py build_ext --inplace
  ```

4. Split the annotation to many files per image and get the image size info.
  ```Shell
  # Check scripts/batch_split_annotation.py,batch_split_annotation.py and change settings accordingly.
  # I modify (**CAFFE_ROOT, coco_data_dir, anno_sets**)
  # Create ImageSets and Annotations in $COCO_ROOT
  python scripts/batch_split_annotation.py
  # Create the val2017_name_size.txt in $CAFFE_ROOT/data/coco
  python scripts/batch_get_image_size.py
  ```

5. Create the LMDB file.
  ```Shell
  cd $CAFFE_ROOT
  # Create the val.txt, testdev.txt, test.txt, train.txt in data/coco/
  python data/coco/create_list.py
  
  # copy .txt to $COCO_ROOT
  
  # You can modify the parameters in create_data.sh if needed.
  # It will create lmdb files for minival, testdev, test, and train with encoded original image:
  #   - $CAFFE_ROOT/data/coco/lmdb/coco_val_lmdb
  #   - $CAFFE_ROOT/data/coco/lmdb/coco_train_lmdb
  # and make soft links at examples/coco/
  ./data/coco/create_data.sh
  ```
