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
result = lda_model.get_neighbours(r'Matthew Brown 9 Kingsbury Street, Norman Park 4170 0401 923 750 mbrown1508@outlook.com 24th August 2013 Suncorp Recruitment PO Box 1453 BRISBANE 4001 Human Resources Manager, Please find my attached application for the Suncorp Group Vacation Program 2013 in the discipline of Information Technology.   I am looking to gain experience at Suncorp so that I can succeed in my Bachelor of Information Technology and hopefully be offered an ongoing role in your graduate program. Currently I am in my second year studying information technology at The Queensland University of Technology (QUT). I have chosen to specialise in Business Process Modelling and I am interested in working for Suncorp as I am aware they have large repositories of BPM models that are used throughout the business. I would hope to learn from people in this discipline at Suncorp while gaining invaluable practical experience in the industry. I think I would be able assist your company as I am a highly motivated and enthusiastic person who always tries to work with a team to get the best result possible. Through my excellent written and verbal communications skills I will be able to effectively communicate to clients and fellow employees to help reach this result. Through my work in the STIMulate peer support program at QUT I have gained invaluable experience working with people helping them reach their potential. This has helped me develop my communication and problem solving skills while improving the QUT community. I feel confident that I will fit into the Suncorp community, have a positive effect on it and fulfil all the tasks asked of me. I have also uploaded my resume and academic transcript as requested. I would greatly appreciate the opportunity to discuss my application with you in more detail. Thank you for taking the time and effort to review my application. Yours sincerely, Matthew Brown')