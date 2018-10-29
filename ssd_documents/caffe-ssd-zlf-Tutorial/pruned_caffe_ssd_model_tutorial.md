1. `git ck prune-dev #切换branch`

2. prune model
   get `.caffemodel, train.prototxt, test.prototxt, deploy.prototxt`

3. generate job and model directores and files
   修改`$CAFFE_ROOT/examples/ssd/zlf_ssd.py`

   ```
   job_name #gen_ssd 下
   run_soon = False
   gen_net_soon = True
   basenet_name 
   pretrain_model
   solver_param_define4train # use gpu that is not used or with enough memory
   ```

   `$CAFFE_ROOT`下运行`python examples/ssd/zlf_ssd.py`

4. 替换model文件夹下对应目录下的`.caffemodel, train.prototxt, test.prototxt, deploy.prototxt` 为prune后文件

5. train pruned model
   修改并运行`zlf_ssd.py`

   ```
   run_soon = True　
   pretrain_model
   gen_net_soon = False
   ```
   plot: `bash parse_log_20181024113127.sh && bash plot_log20181024113127.sh`

6. record model AP and delete sanpshot files except for the needed one

7. merge bn of trained pruned caffemodel and generate timing files
   set `run_soon=False  gen_net_soon=False merge_bn=True` in `zlf_ssd.py` and run it again

8. test and record model speed and GPU memory
   modify to gpu that is not used and run `time**.sh or detect**.sh` in job directory

9. plot detection(optional)
   read `plot_detections**.sh` in job directory and run it, then check the detection result.
