from matplotlib import pyplot as plt

MPL7 = .98
SVM_linear = .9495
SVM_Poly = .9358
SVM_Rbf = .9438
RandomForest = .9824


plt.plot(['MPL', 'SVM(Linear)', 'SVM(Poly)','SVM(Rbf)','Random Forest'], [MPL7, SVM_linear, SVM_Poly, SVM_Rbf, RandomForest], marker='o')
plt.xlabel('Learning Techniques')
plt.title('COMPARITIVE ANALYSIS')
plt.grid(True)
plt.show()
