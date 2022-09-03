from sklearn.metrics import confusion_matrix

def eval_metrics(actual, pred):
    tn, fp, fn, tp = confusion_matrix(actual, pred).ravel()
    return {'acc': (tp+fp)/(tn+tp+fn+fp), 'prec': tp/(tp+fp), 'rec': tp/(tp+fn)}
