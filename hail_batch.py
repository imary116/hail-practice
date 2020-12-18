#########hail batch related#########

##running hail batch on LOCAL backend

#import hail batch first
import hailtop.batch as hb

#define batch
b = hb.Batch(name='practice1')

#define job
#job command to run
for degree in ['BA', 'MS']:
        for school in ['CU', 'BU']:
                j = b.new_job(name=f'{degree}-{school}')
                j.command(f'echo "I did my {degree} at {school}" ')

#run batch
b.run()

##Output:
# I did my BA at CU
# I did my BA at BU
# I did my MS at CU
# I did my MS at BU


##running hail batch on SERVICE backend

#import hail batch first
import hailtop.batch as hb

#setup service backend (don't need to run this command for local backend)
backend=hb.ServiceBackend(billing_project='myohanne-trial', bucket='MY_BUCKET')

#define batch
b=hb.Batch(backend=backend, name='practice2')

#define job
# job command to run
for degree in ['BA', 'MS']:
        for school in ['CU', 'BU']:
                j = b.new_job(name=f'{degree}-{school}')
                j.command(f'echo "I did my {degree} at {school}" ')

#run batch
b.run()

##Output similar to the local backend example above
