import pandas
import pickle
import redis
from datetime import datetime

redis_instance = redis.StrictRedis(host='localhost', port=6379)

file_path = '/opt/pandas-test/star200.csv'

startTime = datetime.now()
data = pandas.read_csv(file_path, error_bad_lines=False)
print('Loading took: %s' % (datetime.now() - startTime))

print(
    'Document type: %s, document size: %s' % (type(data), data.shape))

startTime = datetime.now()
pickled_data = pickle.dumps(data)
print('Pickling took: %s' % (datetime.now() - startTime))

startTime = datetime.now()
redis_instance.set('star200', pickled_data)
print('Shoving into redis took: %s' % (datetime.now() - startTime))

startTime = datetime.now()
pickled_data_from_redis = redis_instance.get('star200')
print('Retrieving from redis took: %s' % (datetime.now() - startTime))

startTime = datetime.now()
unpickled_object = pickle.loads(pickled_data_from_redis)
print('Unpickling took: %s' % (datetime.now() - startTime))

print('Document type: %s, document size: %s' % (
    type(unpickled_object), unpickled_object.shape))
