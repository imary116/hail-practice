#########cluster related######### 

#choose between projects, first run 
gcloud init 

#start a cluster on the cloud with hail predownloaded
hailctl dataproc start mty --region us-central1	

#connect to a jupiter notebook
hailctl dataproc connect mty notebook --zone us-central1-a 
	
#stop a cluster (which you need to do at the end ALWAYS) 
hailctl dataproc stop mty --region us-central1

