# Diploma
My bachelor work in Hochschule Merseburg written in Python, using Native Language Processing of ML

###### My bachelor thesis is: ***Classification of advertisements by means of supervised learning methods ***

#### Work process:
- [X] Learn about NLP
- [X] Scrap data
- [X] Try NLTK / spacy on datasets
- [X] Learn more about hclustering algorithms / Neural networks / Other NLP methods like Topic Modelling, W2W and so on
- [X] Code the Diploma
- [X] Write a Diploma itself = Thesis


#### My bachelor has two major branches: 
1. **Data**
    - Scrapping data from web using scapy, google useragent or proxies. I used to scrap amazon with proxie, but because of lagging and switching off decided to use useragent and time.sleep()
2. **ML**
    - Code implemenation 
    
#### Commits
>One of the 2 branches above: subproject: message. _Not including README.md_. 

__Example:__ 
>> `Data: amazon: added new spider`

>> README.md: update

#### Data comes from these websites:
- [x] obszone
    - had problems downloading american products for sale, so had to use a litle trick with url
-  [x] geebo
- adlandpro
- pennysaverusa
- hoobly
- oodle
- gumtree
- letgo
- salespider
- ebay
-  [X] amazon


## Amazon data issues:
When entering _departments_ on amazon you can scrap either **400** pages of `common` products of said department, or go into ***Feature Categories*** and scrap `precise` products.  
For instance: 400 pages of **automotive** department **OR** *Car care, car electronics* and so on.
