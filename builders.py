from kivy.lang.builder import Builder
import glob 



for each_kv_file in glob.glob('./kv/*.kv'):
    Builder.load_file(each_kv_file)
