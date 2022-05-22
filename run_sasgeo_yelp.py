from recbole.quick_start import run_recbole



parameter_dict = {
   'neg_sampling': None,
}
config_file_list = ['sas_f_yelp.yaml']
run_recbole(model='SASGEO', dataset='yelp', config_file_list=config_file_list, config_dict=parameter_dict)
