# Get data
from worker.getseekjobdescription import GetSeekJobDescription
GetSeekJobDescription()

# Build Model
from worker.buildlda import BuildLda
lda_model = BuildLda()
lda_model.build_object()
from sklearn.externals import joblib
joblib.dump(lda_model, 'worker/pickled_model/lda_model.pkl')

# Load Model
from sklearn.externals import joblib
lda_model = joblib.load('worker/pickled_model/lda_model.pkl')

# Get results
result = lda_model.get_neighbours(r'This is a test to check if the kNN is working')