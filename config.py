from configparser import ConfigParser

CHARPROTLEN = 25
CHARISOSMILEN = 64


class Config():
    def __init__(self):
        # model parmeters
        self.use_gpu = True
        self.gpu = 1
        self.result_path = 'result'
        self.hidden_dim = 512  

        self.tau = 0.5  
        self.l_c = 0.16  # l_c*contrast
        #Drug/Target/Side effect/Disease
        self.sample_rate_d = [8, 1, 80, 180]
        #Drug/Target/Disease
        self.sample_rate_p = [1, 2, 1000]
        self.num_epochs = 40
        self.lam = 0.25

        self.repeat_nums = 1 
        self.fold_nums = 10  # The numbers of crossflod-validation
        self.batch_size = 32

        self.embedding_size = 128           
        self.num_filters = 32
        self.contrast_learn_rate = 0.00001
        self.contrast_epochs = 1

        # Related to the data set
        self.fasta_max_len = 1500  # The max sequense length of protein
        self.smiles_max_len = 150  # The max sequense length of smiles
        self.ds_nums = 5603
        self.se_nums = 4192
        self.dg_nums = 708
        self.pt_nums = 1512
        self.smi_window_lengths = 4
        self.fas_window_lengths = 8
        self.charseqset_size = CHARPROTLEN
        self.charsmiset_size = CHARISOSMILEN

        self.HIN_feat_drop = 0.3
        self.att_drop = 0.5

        self.Nei_d_num = 4
        self.Nei_p_num = 3

        self.dg_ds_path = 'data/drug_disease.csv'
        self.dg_dg_path = 'data/drug_drug.csv'
        self.dg_pt_path = 'data/drug_protein.csv'
        self.dg_se_path = 'data/drug_se.csv'
        self.pt_ds_path = 'data/protein_disease.csv'
        self.pt_pt_path = 'data/protein_protein.csv'

        self.dg_smiles_path = 'data/drug_smiles.csv'
        self.pt_fasta_path = 'data/protein_fasta.csv'

    def set_tau(self, tau):
        self.tau = tau

    def set_l_c(self, l_c):
        self.l_c = l_c

    def set_lam(self, lam):
        self.lam = lam
