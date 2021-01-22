#run coverage ~5min to run  
samtools coverage ~/Desktop/Broad/tj/samtools/sc_global_japan_rik_Huang_Yoshikawa_schizophrenia_exome-RP-1855-Exome-JP-RIK-C-00070-v1-JP-RIK-C-00070.cram -o ~/Desktop/Broad/tj/samtools/output

#run coverage with specified region <1min to run; had to have the .cram.crai file in the same directory as the .cram file  
samtools coverage -r chr1:1M-12M ~/Desktop/Broad/tj/samtools/sc_global_japan_rik_Huang_Yoshikawa_schizophrenia_exome-RP-1855-Exome-JP-RIK-C-00070-v1-JP-RIK-C-00070.cram -o ~/Desktop/Broad/tj/samtools/output2
