# Turkish-SAD

This repository provides a collection of Turkish Sentiment Analysis Datasets from 2012 to 2022, covering various domains. It includes access links for publicly available datasets and contact information for non-public datasets.  It also includes a Python script for sentiment analysis using pre-trained transformer models. 

## Turkish Sentiment Analysis Datasets

A thorough investigation was carried out on research papers related to 'sentiment analysis' and 'Turkish dataset' indexed on Scopus between 2012 and 2022. 23 unique datasets were collected from publicly available sources and through email requests. This repository provides links to the publicly available Turkish datasets, as well as contact information for those that are not publicly available.

### Search Details:
- **Search Query:** `'sentiment analysis' AND 'Turkish dataset'`
- **Fields:** Article Title, Abstract, Keywords
- **Date Range:** 2012–2022
- **Database:** Scopus

The repository provides:
- **Links** to publicly available datasets.
- **Contact Information** for datasets not openly accessible.

---

## Contents

1. [List of Datasets](#list-of-datasets)
2. [Usage](#usage)
3. [Requirements](#requirements)
4. [Pre-trained Models](#pre-trained-models-used)
5. [Using Google Colab](#using-google-colab)

## List of Datasets

| Author(s), Year (with link)                                                                                   | Dataset Name (with download link if available)                                                 | Source                               | Availability     | Notes / Contact / Reuse Info                                                                                             |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------|------------------|--------------------------------------------------------------------------------------------------------------------------|
| [Demirtas & Pechenizkiy, 2013](https://dl.acm.org/doi/pdf/10.1145/2502069.2502078)                             | [Turkish Movie Reviews, Turkish Multidomain Product Reviews](https://www.win.tue.nl/~mpechen/projects/smm/#Datasets) | Beyazperde.com, Hepsiburada.com     | Public           | e.demirtas@student.tue.nl, m.pechenizkiy@tue.nl                                                                          |
| [Cetin et al., 2013](http://www.kemik.yildiz.edu.tr/data/File/publications/Text%20Classification%20Clustering/Egiticili%20ve%20Geleneksel%20Terim%20Aglrllklandirma%20Yontemleriyle%20Duygu%20Analizi.pdf) | Telecom Dataset A & B                                                                          | Twitter                              | Not Available    | cetinmahmut@msn.com, mfatih@ce.yildiz.edu.tr                                                                             |
| [Isguder & Sahin, 2014](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6973514)                      | Ekşi Sözlük Technology Brand Comments Dataset                                                  | Ekşi Sözlük                          | Not Available    | isguderg@itu.edu.tr, harunzafer@gmail.com, adali@itu.edu.tr                                                              |
| [Turkmenoglu & Cadırci, 2014](https://d1wqtxts1xzle7.cloudfront.net/108813139/download_jsessionid_00E6A9E756589AC939F407A7F15D5AA8-libre.pdf) | Twitter Dataset, Movie Dataset                                                                  | Twitter, Beyazperde.com              | Not Available    | turkmenogluc@itu.edu.tr, tantug@itu.edu.tr                                                                              |
| [Coban et al., 2015](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7130362)                             | Twt                                                                                             | Twitter                              | Not Available    | onder.coban@atauni.edu.tr, baris.ozyer@atauni.edu.tr, gulsah.ozyer@atauni.edu.tr                                       |
| [Ekinci & Güler, 2016](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7495714)                        | Turkcell Twitter Dataset, TTNet Twitter Dataset                                                 | Twitter                              | Not Available    | meryemeknc@gmail.com, saidozcn@gmail.com, mfatih@ce.yildiz.edu.tr                                                       |
| [Ogul, 2016](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7495786)                                 | Hotel Reviews Dataset                                                                           | Booking.com, Tripadvisor.com         | Not Available    | n14241878@cs.hacettepe.edu.tr, gonenc@cs.hacettepe.edu.tr                                                                |
| [Parlar, 2016](https://www.researchgate.net/profile/Tuba-Parlar/publication/308570079_A_new_feature_selection_method_for_sentiment_analysis_of_Turkish_reviews/links/5a2179110f7e9b71dd031791/A-new-feature-selection-method-for-sentiment-analysis-of-Turkish-reviews.pdf) | Turkish Multidomain Product Reviews | Hepsiburada.com | Public           | *Reused* *from [Demirtas & Pechenizkiy, (2013)](https://www.win.tue.nl/~mpechen/projects/smm/#Datasets)*  |
| [Ucan et al., 2016](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7475237) | [Movie Review, Hotel Review](http://humirapps.cs.hacettepe.edu.tr/tsad.aspx) | Beyazperde.com, Otelpuan.com | Public | ebru@hacettepe.edu.tr, aucan@hacettepe.edu.tr, n.behzad@hacettepe.edu.tr, sever@hacettepe.edu.tr |
| [Ayata et al., 2017](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7960519) | [Retail, Telecom, Football, and Banking Tweets](https://www.baskent.edu.tr/~msert/research/datasets/SentimentDatasetTR.html) | Twitter | Public | ahayran@baskent.edu.tr, msert@baskent.edu.tr |
| [Parlar, Saraç & Özel, 2017](https://www.researchgate.net/publication/318037151_Comparison_of_feature_selection_methods_for_sentiment_analysis_on_Turkish_Twitter_data) | Turkish Twitter Dataset | Twitter | Not Available | *Reused from Çetin & Amasyalı (2013)* tparlar@mku.edu.tr esrasarac@adanabtu.edu.tr saozel@cu.edu.t |
| [Hayran & Sert, 2017](https://ieeexplore.ieee.org/document/7960519) | [Turkish Sentiment Dataset](https://www.baskent.edu.tr/~msert/research/datasets/SentimentDatasetTR.html) | Twitter | Public | ahayran@baskent.edu.tr, msert@baskent.edu.tr |
| [Omurca, Ekinci & Türkmen, 2017](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8090212) | [Turkish Hotel Review Dataset (annotated)](http://dx.doi.org/10.13140/RG.2.2.13338.44488) | Otelpuan.com | Public | silhan@kocaeli.edu.tr ekin.ekinci@kocaeli.edu.tr hazal.turkmen@kocaeli.edu.tr |
| [Mulki, Haddad, Ali & Babaoğlu, 2018](https://doi.org/10.1109/SIU.2018.8404718) | Turkish Movie & Multidomain Product Reviews | Hepsiburada.com | Public           | *Reused* *from [Demirtas & Pechenizkiy, (2013)](https://www.win.tue.nl/~mpechen/projects/smm/#Datasets)*  |
| [Yüksel & Tan, 2018](https://hrcak.srce.hr/file/328239) | [Foursquare Venue and Comments Data](https://data.mendeley.com/datasets/29tbvvwkdp/2) | Foursquare | Public | asimyuksel@sdu.edu.tr |
| [Ay Karakuş, Talo, Hallaç & Aydın, 2018](https://doi.org/10.1002/cpe.4783](https://www.researchgate.net/profile/Betul-Ay-2/publication/326443062_Evaluating_deep_learning_models_for_sentiment_classification/links/5b5087fa0f7e9b240fede03d/Evaluating-deep-learning-models-for-sentiment-classification.pdf) | [Turkish Movie Reviews Dataset](http://buyukveri.firat.edu.tr) | Beyazperde.com | Public | betulaykarakus@gmail.com, mtalo@firat.edu.tr, irhallac@firat.edu.tr, gaydin@firat.edu.tr |
| [Yurtalan, Koyuncu & Turhan, 2019](https://journals.tubitak.gov.tr/cgi/viewcontent.cgi?article=1724&context=elektrik) | Turkish Twitter Dataset | Twitter | Not Available | mkoyuncu@atilim.edu.tr |
| [Amasyalı, Taşköprü & Çalışkan, 2018](https://doi.org/10.1109/ASYU.2018.8554037) | [Turkish Telecom Twitter Dataset](https://github.com/mfatihamasyali/sentiment_deep_or_classical) | Twitter | Public | mfatih@ce.yildiz.edu.tr, hakantaskopru77@gmail.com, kubra.clskn94@gmail.com |
| [Çiftçi & Apaydın, 2019](https://doi.org/10.1109/IDAP.2018.8620751) | Turkish Product & Movie Reviews Dataset | Hepsiburada.com & Beyazperde.com | Not Available | basri.ciftci@std.sehir.edu.tr apaydin@sehir.edu.tr |
| [Çoban & Özyer, 2018](https://doi.org/10.1109/IDAP.2018.8620757) | [VS1 - 3000 Turkish Tweets](http://www.kemik.yildiz.edu.tr/data/File/3000tweet.rar), [VS2 - *Reused from Hayran & Sert (2017)](http://www.baskent.edu.tr/~msert/research/datasets/SentimentDatasetTR.html)* | Twitter | Public | ocoban@cu.edu.tr gulsah.ozyer@atauni.edu.tr |
| [Oğul & Güran, 2019](https://doi.org/10.1109/UBMK.2019.8907041) | VS1 - [SemEval-2017 Task 4](http://alt.qcri.org/semeval2017/task4/index.php?id=download-thefull-training-data-for-semeval-2017-task-4), VS2 - *Reused from [Amasyalı et al. (2018)](https://github.com/mfatihamasyali/sentiment_deep_or_classical)*, VS3 - [CrowdFlower Airline Dataset](https://www.kaggle.com/crowdflower/twitter-airline-sentiment) | Twitter | Public | 20172105039@dogus.edu.tr adogrusoz@dogus.edu.tr | 






















| Articles     | Datasets           | Status      | Contact Info |
| ------------------ | ---------------------- | ----------------- | --- |
| [Cross-lingual Polarity Detection with Machine Translation](https://dl.acm.org/doi/pdf/10.1145/2502069.2502078?casa_token=RpBnOZk_7IEAAAAA:zxehldkECOfZPAr83Mdys0EZxSpQgKMYzhiiCzhKc1sFRH8dcXnqfr6QecAK_vZZAP6mzMB-TeHU)    | [Turkish Movie Reviews & Turkish Multidomain Products Reviews](https://www.win.tue.nl/~mpechen/projects/smm/#Datasets) | Publicly Available | e.demirtas@student.tue.nl m.pechenizkiy@tue.nl|
| [Sentiment Analysis on Turkish Telecom Related Tweets](http://www.kemik.yildiz.edu.tr/data/File/publications/Text%20Classification%20Clustering/Egiticili%20ve%20Geleneksel%20Terim%20Aglrllklandirma%20Yontemleriyle%20Duygu%20Analizi.pdf) | Telecom Dataset A & B | Not Available | cetinmahmut@msn.com mfatih@ce.yildiz.edu.tr |
| [Sentiment Analysis on Ekşi Sözlük Technology Brand Entries](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6973514) | Ekşi Sözlük Technology Brand Comments Dataset | Not Available | isguderg@itu.edu.tr harunzafer@gmail.com adali@itu.edu.tr |
| [Sentiment Analysis in Turkish Media](https://d1wqtxts1xzle7.cloudfront.net/108813139/download_jsessionid_00E6A9E756589AC939F407A7F15D5AA8-libre.pdf?1702374670=&response-content-disposition=inline%3B+filename%3DSentiment_Analysis_in_Turkish_Media.pdf&Expires=1718288020&Signature=hIs~pjmOQj8v3IZhG~8a2hcBwBJZUOdzHJkj6T6ymw5sl865l64yuL0i5fmMRDm3~VL5PNvFAl3FFrDNKSiTD1PW3r3hbcZVyV-hfvghAuGl5kvgxMKzmt0Xjkzn35QlQfnWNm~pzA~mF6kbTx2KHJhWTrWiwd-m2vx-eSSoGCQjxkJKxBu5nZ-fauaKes3MWNfVqrp1y1DZRZJBOLP71phdfHXeDWGVBPbjZfdbrrwRgKXwLt2K4rhHIsJDKnfwQQ19WyqdUyGEJd4gAHZ~qybJcN6kCcGFzbgjjiLOw~81Rg2rLGqFqwdbRz0sY77n~jzb6s9vliXRwgoF35GBIQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA) | Twitter Dataset & Movie Dataset | Not Available | turkmenogluc@itu.edu.tr tantug@itu.edu.tr |
| [Sentiment Analysis for Turkish Twitter Feeds](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7130362&casa_token=vmqnO6gQ10cAAAAA:b9WagYcf23lutBy5cRr_osVl2blL418bpKYYgA_X_t1J2Td70uXciUzPJp1umnSEA5Iu9rEX-w&tag=1)| Twt | Not Available | onder.coban@atauni.edu.tr baris.ozyer@atauni.edu.tr gulsah.ozyer@atauni.edu.tr|
| [Time Effect in Turkish Sentiment Analysis]([https://ab.org.tr/ab16/bildiri/AB16-93.pdf](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7495714)) | Turkcell Twitter Dataset & TTNet Twitter Dataset | Not Available | meryemeknc@gmail.com saidozcn@gmail.com mfatih@ce.yildiz.edu.tr  |
| [Sentiment Analysis on Hotel Reviews in Turkish with Supervised Learning Algorithms](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7495786) | Hotel Reviews Dataset | Not Available | n14241878@cs.hacettepe.edu.tr gonenc}@cs.hacettepe.edu.tr |
| [A New Feature Selection Method for Sentiment Analysis of Turkish Reviews]([https://ab.org.tr/ab16/bildiri/AB16-55.pdf](https://www.researchgate.net/profile/Tuba-Parlar/publication/308570079_A_new_feature_selection_method_for_sentiment_analysis_of_Turkish_reviews/links/5a2179110f7e9b71dd031791/A-new-feature-selection-method-for-sentiment-analysis-of-Turkish-reviews.pdf)) | Turkish Multidomain Product Reviews *(reused from [Demirtas & Pechenizkiy, 2013](https://www.win.tue.nl/~mpechen/projects/smm/#Datasets))* | Publicly Available | turgay.parlar@bilecik.edu.tr |
| [SentiWordNet for New Language: Automatic Translation Approach](https://d1wqtxts1xzle7.cloudfront.net/65130268/07907484-libre.pdf?1607414911=&response-content-disposition=inline%3B+filename%3DSentiWordNet_for_New_Language_Automatic.pdf&Expires=1718805097&Signature=ezUBmNpJ6-fXT2dhe9OEn338g1YiMFwsptGvwQy4z~G6n-Es-rev7gUQxk-r8RyqMIKRXW0WJoWHlwmSZIF7hPE8BQhtTRzFeePYimrU9U7KPXb9fNSwh6QuXeTfTpk1c~nw~WY9PsajEw3sO2q10euvH4fym5cXRubk6uVP2wUmVhsCu-j-iqE80v66i4ihS75lQcifgciyYfVisyew6nC5MbYz9mz~7N2OufbdzAO1Hq~gZZlZIR1q3dIXB16BQJpmXpdqtNDR5vNRERpcWxjNfP3ffGi0ISVddPHKphiEj9OWx2C3gymx28b1jCpDVX8mFvPQM5X3E2c5CRpcYw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)| [Turkish Sentiment Analysis Dataset](http://humirapps.cs.hacettepe.edu.tr/tsad.aspx) | Publicly Available | aucan@hacettepe.edu.tr n.behzad@hacettepe.edu.tr ebru@hacettepe.edu.tr sever@hacettepe.edu.tr |
| [Sentiment Analysis on Microblog Data based on Word Embedding and Fusion Techniques](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7960519) | [Turkish Sentiment Dataset](https://www.baskent.edu.tr/~msert/research/datasets/SentimentDatasetTR.html) | Publicly Available | ahayran@baskent.edu.tr msert@baskent.edu.tr |
| [A Real-time Social Network-based Knowledge Discovery System for Decision Making](https://hrcak.srce.hr/file/328239) | [Foursquare Venue and Venue Comments Data](https://data.mendeley.com/datasets/29tbvvwkdp/2) | Publicly Available | asimyuksel@sdu.edu.tr |
| [Words, Meanings, Characters in Sentiment Analysis](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8554037) | [Dataset](https://github.com/mfatihamasyali/sentiment_deep_or_classical) | Publicly Available | mfatih@ce.yildiz.edu.tr hakantaskopru77@gmail.com kubra.clskn94@gmail.com | 
| [Sentiment Analysis Through Transfer Learning for Turkish Language](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8778305&casa_token=XDgXfdiAdz8AAAAA:e3h6HWTt92lPs9GOtCXjZQWOFYPI2bHzxPNgoxTLxzpKJCIs7MPp-8OkQYhzLaogbgpIJ2_FaQ) | [Turkish Product Reviews Dataset](https://github.com/fthbrmnby/turkish-text-data) | Publicly Available | emre.akin02@bilgiedu.net tugba.yildiz@bilgi.edu.tr |
| [Sentiment Analysis in Turkish Text with Machine Learning Algorithms](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8946436) | Dataset | Not Available | merve.rumelli@ceng.deu.edu.tr deniz.akkus@ceng.deu.edu.tr ozge.kart@deu.edu.tr zerrin@cs.deu.edu.tr | 
| [Sentiment Analysis of Turkish Twitter Data](https://watermark.silverchair.com/080004_1_online.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAABX4wggV6BgkqhkiG9w0BBwagggVrMIIFZwIBADCCBWAGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMGeA0MMqVAinFop1ZAgEQgIIFMf92TiLj_AeQmds0l1lZ1hYtTIQpUbnRS8jsLy_dwUkolxYgHx2Urz5rE3g3zMtBCloHT8R1gQvmv7Kyd2XG_H-Ta8cNtDBptmrxFA8qVUfbELKqwQu4N_fVZqIO50Khl9sMiRArSSWUwM9P6wQSTZUKFgC0V1qC2T8qEdtXyQUHdv5uagkI4TmYbUb89HkXIjyF3xlN93oDd8Ph5tB0Ji7bXzpdeCH9NUeeF9PDXKEFJbwxDL3xP_XuNaKpE3npQ7isMKKXTbBN317PTrr6hr1oa_xSmnnvfWwkTnpQZ_sJLICo3enyxo4CsrLQvdYeaYOUxoPhoikZYhHh8o7UXRgvDlt2y11V1x5Og0RO-_U6HKTwEH6cxNLUYiTw1gkP0R3culTscG8pXFvEM8KeasTm6K-r7lf3TFLpkqWvCkWYMlsiq1U5nFD9DEoogEckRlcS5xodph51B1zw5k4NKaOIc2uYLkMpmfP9m-ebsArIZR1m9Y9JsyKOyM_9__o3F81sSudxcUxd2EFp8ngXFxugbHEgC8E7N6lRo2dwfcG0-ByFzDHA19juhGDDM5lT8qdceQ8Ja6daDLL-J9eZR3McayYQ8FzGY5fGj2WYKRj-0cpKGmqGsIoyNne3FzUQLtoU2WRhlcsKAwbjSZFlOQ0EBLTbjA9deFmW9QDydIPV6TdhRITnjPa1fdbxFNkMwBYwAGVdOJK7HA2dCQuQ9-i21g9a9yg-B7ywKALRre82taJWmNItMJI_VF1TJ-0egPlm_dxvZpClzogw0MkLDNpQh5CCrqOi4JASKdoVXrf8YnnsCizcDzIkYB6SacNlzxBgy6QiPlNaTu7JwSW-uwh5CBVjUw_rKHOv00gbvT4ugf2fn4Ay-cd1tp02k_wuH7wMB8DCv-fWxvuQV9ul1zqD-oZYyTbjMg7GHEk6FASacTIXunzVsOlgFo19WZXfGMdldUwosaumRiobaDUhHt_4scxtR7kRkeLWbmY2NEsV0kN9VdcMAn-43-FqL62OjciR0u-Jd25X51gcsb5lTR1ir_4C_gWNizoOd4Ks2Y631-FvYXufFfiq2uPa64rGikxs8TOMqUQ6mm698ec_uJjCWb7T_-B2qGTFS5mVZGKj8TlqOyLK7J0aVWR7QVvPBNRgH9E4seNLFJLPwWZ5yOjH7v9wNuUCTy_GwVKf0bf_B43KUsyZiP6LC3TZHfHv0UDNQF8dr1SF14o-F5kS3dkGveAp0u0y3PTNe1Py89WGD3eimXzMPWn_eC6yOKqr9jsanYB2WLlTqFtxFupUAkj2aGEVh6yXSJypcpP4kMprc8FbaLV-i_5M0mx_jCoOBn1mBLO5iWM-mgHDoaVy2CoxjHiuRWccFHoo2t3JBenUh2x09QkJoHcVFLosF6I3GT9WdgjCFO_XgM1Nt-i3n7dKYtdfIr6DSt0zf7SQKByvukPABRUK7r2v3Bm6FzQFiNC88-8xR2wjX2teho8CYWzp53135tARXsCDqFu4pQeJvU6mpZW_OTpNQfXdJWJFZDWW0ZMCxp1CIu8HVl1aAE2OQ2pXDjSH4oHTaJ5eYlt_wj-WGr0R2QOQk_UtmR3knoChGSTTB6TVr1o28ZAKBTcE9zcwbL3CFc4aGIP_fJDxqeU-lrNCcismMm7EuagipF3csYorbJWEWHbPYXUBYDdNgt6TSQs18VaIE03CWFqeF5msu2cAAyPZKrDWC90FqdIgh_tmbbezrBdD3tVuiyUM8IA-mAErfKXEXjq7JF_58A) | Dataset | Not Available | harisushehu@gmail.com stokat@pau.edu.tr md.sharif@uoh.edu.sa uyaver@tau.edu.tr |
| [Comparison of N-stage Latent Dirichlet Allocation versus Other Topic Modeling Methods for Emotion Analysis](https://avesis.yildiz.edu.tr/yayin/713d263f-bb7a-49a5-92e3-130515d6d02c/comparison-of-n-stage-latent-dirichlet-allocation-versus-other-topic-modeling-methods-for-emotion-analysis) | Dataset | Not Available | zekeriya.anil.guven@ege.edu.tr diri@yildiz.edu.tr txcakaloglu@ualr.edu |
| [An Annotated Turkish Aspect Based Sentiment Analysis Corpus for Smart Tourism](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9599037) | [Turkish Tourism ABSA Dataset](https://github.com/salurumut/Turkish-Aspect-Based-Sentiment-Analysis-Corpus-for-Smart-Tourism) | Publicly Available | mehmetumut.salur@gibtu.edu.tr iaydin@firat.edu.tr |
| [Twitter Dataset and Evaluation of Transformers for Turkish Sentiment Analysis](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9477814&casa_token=x9OIXvmFAcYAAAAA:O0iEKC4ozn_WZ0UWZAKFtyhll-FJAv5GVHb2st2rLXy5QPAAO7-E10HcEB-xG3IfRMBN3cGggw) | [BounTİ Turkish Sentiment Analysis](https://github.com/boun-tabi/BounTi-Turkish-Sentiment-Analysis) | Publicly Available | abdullatif.koksal@boun.edu.tr arzucan.ozgur@boun.edu.tr |
| [Aspect Based Twitter Sentiment Analysis on Vaccination and Vaccine Types in COVID-19 Pandemic With Deep Learning](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9640526&casa_token=by-s7bN7B8wAAAAA:FHLwDVxCTBaAlhBn6HQeeXOInW8OFPni-83tVN6P8sM97ZGbDECwIsZcIcc2A_ymIugqmBH0YQ) | [Covid 19 Vaccination Dataset](https://github.com/IrfanAygun/Covid-19-Vaccination-Dataset-and-Sentiment-Analysis) | Publicly Available | irfan.aygun@cbu.edu.tr bkaya@firat.edu.tr kaya@firat.edu.tr |
| [TRSAv1: A New Benchmark Dataset for Classifying User Reviews on Turkish E-commerce Websites](https://journals.sagepub.com/doi/pdf/10.1177/01655515221074328?casa_token=SLDsalgZ0ocAAAAA:BCfUE8HCg62kFfbNKJUJIrEHRIGly74-6uLd1ibIIOI7sWtDuoDu2pschxtGze4Oyhg26bJoUWP_) | [TRSAv1](https://github.com/maydogan23/TRSAv1-Dataset) | Publicly Available | m.aydogan@firat.edu.tr |
| [Multi-Label Classification of E-Commerce Customer Reviews via Machine Learning](https://www.mdpi.com/2075-1680/11/9/436) | [Turkish E-Commerce Reviews Dataset](https://github.com/emredeniz18/data) | Publicly Available | mustafacosar@hitit.edu.tr |
| [Sentimental Analysis of Twitter Users from Turkish Content with Natural Language Processing](https://onlinelibrary.wiley.com/doi/pdf/10.1155/2022/2455160) | [The Public Dataset](https://www.kaggle.com/datasets/mrtbeyz/trke-sosyal-medya-paylam-veri-seti) & [SentimentSet](https://www.kaggle.com/datasets/caglaballi/sentimentset) | Publicly Available | alok.mishra@himolde.no |
| [A Dataset and BERT-based Models for Targeted Sentiment Analysis on Turkish Texts](https://arxiv.org/pdf/2205.04185) | Dataset | Not Available | melih.mutlu@boun.edu.tr arzucan.ozgur@boun.edu.tr |
| [A Novel COVID-19 Sentiment Analysis in Turkish based on the Combination of Convolutional Neural Network and Bidirectional Long-short Term Memory on Twitter](https://onlinelibrary.wiley.com/doi/pdf/10.1002/cpe.6883?casa_token=60k59dpfdCkAAAAA:fdTiJ7U4gU1dZ2xJCoVTKqs1VWPjn8nyFXCZnhixv6hzmfgmxZukp3ib2CZ-OFudsTVukG6vypUGPQ) | COVID-19 Dataset | Not Available | talhakabakus@duzce.edu.tr |
| [Opinion Mining Using LSTM Networks Ensemble for Multi-class Sentiment Analysis in E-commerce](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9998264) | Dataset | Not Available | dalnahas@infina.com.tr fasik@infina.com.tr akanturvardar@infina.com.tr mulkgun@infina.com.tr | 
| [BERT-based Transfer Learning Model for COVID-19 Sentiment Analysis on Turkish Instagram Comments](https://www.itc.ktu.lt/index.php/ITC/article/view/30276) | Dataset1 & Dataset2 | Not Available | d2014242@mersin.edu.tr akdagli@mersin.edu.tr caci@mersin.edu.tr |


## Usage

### Steps to Use:
1. Clone this repository:
   ```bash
   git clone https://github.com/sevvalckc/Turkish-SAD.git
   cd Turkish-SAD
2. Install required libraries:
   pip install -r requirements.txt
3. Ensure your datasets (e.g., data1.csv, data2.csv) are placed in the same directory as the script.
4. Run the script:
   python sentiment_analysis.py
5. The script will output sentiment analysis results to CSV files for each model.


## Requirements
The script requires the following Python libraries and versions:
- Pandas version: 2.2.2
- PyTorch version: 2.5.1+cu121
- Transformers version: 4.46.2
- Scipy version: 1.13.1

## Install Requirements
To install all required libraries, run:
pip install -r requirements.txt
sv) for each model.

## Pre-trained Models Used

TurkishBERTweet: VRLLab/TurkishBERTweet-Lora-SA
TSAM: emre/turkish-sentiment-analysis
BERTurk: akoksal/bounti
XLM-T: cardiffnlp/twitter-xlm-roberta-base-sentiment

## Using Google Colab

Enabling TPU and High RAM

To use this script on Google Colab with TPU and high RAM, follow these steps:

- Open Google Colab: Go to Google Colab.
- Upload the script: Upload sentiment_analysis.py and your datasets (data1.csv, data2.csv) to Colab.

Enable TPU:

Go to Runtime > Change runtime type.
Select TPU from the Hardware accelerator dropdown menu.
Enable High RAM:

Go to Runtime > Manage sessions.
Click on the current session.
Select High-RAM from the options available.


