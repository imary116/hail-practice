## cluster related 

# choose between projects, first run 
gcloud init 

# start a cluster on the cloud with hail predownloaded
hailctl dataproc start mty --region us-central1	

# connect to a jupiter notebook
hailctl dataproc connect mty notebook --zone us-central1-a 
	
# stop a cluster (which you need to do at the end ALWAYS) 
hailctl dataproc stop mty --region us-central1

## hail batch related 

## running hail batch on local backend

# import hail batch first 
import hailtop.batch as hb 
  
# define batch
b = hb.Batch(name='practice1') 

# define job 

# job command to run 
for degree in ['BA', 'MS']: 
	for school in ['CU', 'BU']:
		j = b.new_job(name=f'{degree}-{school}')
		j.command(f'echo "I did my {degree} at {school}" ')


# run batch
b.run()

## Output:
# I did my BA at CU
# I did my BA at BU
# I did my MS at CU
# I did my MS at BU 

