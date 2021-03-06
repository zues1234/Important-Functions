# -*- coding: utf-8 -*-
"""Important features in naive bayes classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gSP1iZZ5ZC3jJQDpcJbNDYHiWSYNYZKg
"""



"""Suppose we have a naive bayes classifier "clf". we can get the coefficients from it using "clf.coef_" which are helpful in getting the important features/ words from text field.

for ex:
"""

indices = np.argsort(-1.abs(clf.coef_)[predicted_class - 1][:,:no_of_features])
# this will return the array of postive integer values(used -1*abs) of shape (1,-1)
# these values will then be compared with previous length of count vectorizers like for eg
# gene, variation, text feature
def(index, text, gene, var) # check importamce of query point

for i, v in enumerate(indices[0]) #[[a,b,c,d,e,f....]]
# value if less than the len of no of features in gene
# than we would get the word from gene features(gene_vec = countVectorizer, gene_vec.get_feature_names()[v])
# whose index is the value of indices (more in code)
  if v < no_of_feat_in_gene:
    word = gene_vec.get_feature_names()[v]
# if the value is les than (v< len of no of feature names from gene and variation)
# then we get the word from variation feature names whose index is v-sum of no of feat in gene and var
if v < (no_of_feat_in_gene + no_of_feat_in_variation):
    word = var_vec.get_feature_names()[v-(no_of_feat_in_gene + no_of_feat_in_variation)]

# after we get the word we check if thet word in present in query text or not 
#if present we print the word
if v < no_of_feat_in_gene:
    word = gene_vec.get_feature_names()[v]
    yes_no = True if word in text.split("") else false:
    if yes_no:
      word_count += 0
      print(i, gene feature "word" present in query text point)

# this function will be used just for naive bayes
# for the given indices, we will print the name of the features
# and we will check whether the feature present in the test point text or not
def get_impfeature_names(indices, text, gene, var, no_features):
    gene_count_vec = CountVectorizer()
    var_count_vec = CountVectorizer()
    text_count_vec = CountVectorizer(min_df=3)
    
    gene_vec = gene_count_vec.fit(train_df['Gene'])
    var_vec  = var_count_vec.fit(train_df['Variation'])
    text_vec = text_count_vec.fit(train_df['TEXT'])
    
    fea1_len = len(gene_vec.get_feature_names())
    fea2_len = len(var_count_vec.get_feature_names())
    
    word_present = 0
    for i,v in enumerate(indices):
        if (v < fea1_len):
            word = gene_vec.get_feature_names()[v]
            yes_no = True if word == gene else False
            if yes_no:
                word_present += 1
                print(i, "Gene feature [{}] present in test data point [{}]".format(word,yes_no))
        elif (v < fea1_len+fea2_len):
            word = var_vec.get_feature_names()[v-(fea1_len)]
            yes_no = True if word == var else False
            if yes_no:
                word_present += 1
                print(i, "variation feature [{}] present in test data point [{}]".format(word,yes_no))
        else:
            word = text_vec.get_feature_names()[v-(fea1_len+fea2_len)]
            yes_no = True if word in text.split() else False
            if yes_no:
                word_present += 1
                print(i, "Text feature [{}] present in test data point [{}]".format(word,yes_no))

    print("Out of the top ",no_features," features ", word_present, "are present in query point")