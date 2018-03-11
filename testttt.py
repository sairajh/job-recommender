''' Install RAKE in PC by typing "pip install rake-nltk" in cmd window. Whole line should look like "C:>pip install rake-nltk" '''


from rake_nltk import Rake

r = Rake()

mytext = '''Spesso is a vegetarian restaurant that will live upto all your expectations if you're a vegetarian. We tried the Mexican Quesadillas and a thin crust Piccante Pizza. To be honest we've had better pizzas, overall it was an average pizza with nothing extraordinary about it. The Pizza and Quesadillas were definitely not our most favourite dishes for the day. Next we ordered the Primavera gourmet pasta. The pasta was amazing in every bite and left us for wanting more of its heavenly creaminess. For dessert we had the famous Hazelnut Chocolate Pot. Spesso's signature dessert won't fail to make you fall in love with it. They have a very quick service and a friendly staff. Also, they have an impressive quantity of anything you order. Overall Spesso is a little overpriced but they're providing 15% off on lunch if you show your visiting card. So hurry as we definitely recommend it for vegetarian lovers for a flavorsome gastronomical experience!
Foodscapades Rates: 8/10'''

r.extract_keywords_from_text(mytext)

r.get_ranked_phrases()

r.get_ranked_phrases_with_scores()

print(r.get_ranked_phrases_with_scores())
