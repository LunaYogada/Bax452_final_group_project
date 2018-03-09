model2 = GradientBoostingClassifier(learning_rate=0.2, random_state=3,
                    n_estimators=180, subsample=0.78, max_depth=10)
	

model2.fit(reserve_date[col], reserve_date['visitors'].values)
print("Model2 trained")


preds2 = model2.predict(test[col])

merge = test[['air_store_id','visit_date']].copy()
merge['preds1'] = pd.Series(preds1)
merge['preds2'] = pd.Series(preds2)
merge['preds3'] = pd.Series(preds3)
merge.head()