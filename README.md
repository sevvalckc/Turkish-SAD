# Turkish-SAD

This repository provides a comprehensive collection of Turkish Sentiment Analysis Datasets from 2012 to 2025, covering diverse domains such as social media, e-commerce, news, political commentary, and more. It includes access links for publicly available datasets, contact information for restricted datasets, and detailed reuse references. Additionally, the repository provides a Python script for sentiment analysis using pre-trained transformer models.


## Turkish Sentiment Analysis Datasets

To build this repository, we systematically reviewed academic studies indexed in Scopus and other scholarly databases. The search focused on publications that applied sentiment analysis using Turkish-language data or introduced sentiment-labeled Turkish datasets. Inclusion criteria required that papers either:
- Used classification models on labeled Turkish sentiment datasets and reported results, or
- Contributed novel Turkish datasets suitable for future modeling.

The final collection includes 78 studies and over 80 datasets. Among these:
- More than 60 datasets are publicly available and linked,
- Others are listed with author contacts for access,
- Reused datasets are referenced with their original sources.

### Search Details:
- **Query:** `'sentiment analysis' AND 'Turkish dataset'`
- **Databases:** Scopus, IEEE Xplore, ACL Anthology, arXiv, MDPI, etc.
- **Document Types:** Conference papers, journal articles, book chapters
- **Date Range:** 2012–2025

The repository includes:
- 📂 **Dataset links** (where available)
- ✉️ **Contact emails** for closed datasets
- 🔁 **Reuse citations**
- 📊 **Metadata** such as domain, size, and labeling method


### Search Details:
- **Search Query:** `'sentiment analysis' AND 'Turkish dataset'`
- **Fields:** Article Title, Abstract, Keywords
- **Date Range:** 2012–2025
- **Databases:** Scopus, IEEE Xplore, arXiv, MDPI, ACL Anthology, and others

The repository provides:
- **Links** to publicly available datasets
- **Contact Information** for datasets that are not openly accessible
- **Reuse Citations** for datasets previously published or used in multiple studies
- **Dataset Metadata** including domain, size, source, and sentiment labeling method


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
| [Parlar, 2016](https://www.researchgate.net/profile/Tuba-Parlar/publication/308570079_A_new_feature_selection_method_for_sentiment_analysis_of_Turkish_reviews/links/5a2179110f7e9b71dd031791/A-new-feature-selection-method-for-sentiment-analysis-of-Turkish-reviews.pdf) | Turkish Multidomain Product Reviews *Reused* *from [Demirtas & Pechenizkiy, (2013)](https://www.win.tue.nl/~mpechen/projects/smm/#Datasets)* | Hepsiburada.com | Public           | tparlar@mku.edu.tr saozel@cu.edu.tr |
| [Ucan et al., 2016](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7475237) | [Movie Review, Hotel Review](http://humirapps.cs.hacettepe.edu.tr/tsad.aspx) | Beyazperde.com, Otelpuan.com | Public | ebru@hacettepe.edu.tr, aucan@hacettepe.edu.tr, n.behzad@hacettepe.edu.tr, sever@hacettepe.edu.tr |
| [Ayata et al., 2017](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7960519) | [Retail, Telecom, Football, and Banking Tweets](https://www.baskent.edu.tr/~msert/research/datasets/SentimentDatasetTR.html) | Twitter | Public | ahayran@baskent.edu.tr, msert@baskent.edu.tr |
| [Parlar, Saraç & Özel, 2017](https://www.researchgate.net/publication/318037151_Comparison_of_feature_selection_methods_for_sentiment_analysis_on_Turkish_Twitter_data) | Turkish Twitter Dataset *Reused from Çetin & Amasyalı (2013)* | Twitter | Not Available | tparlar@mku.edu.tr esrasarac@adanabtu.edu.tr saozel@cu.edu.t |
| [Hayran & Sert, 2017](https://ieeexplore.ieee.org/document/7960519) | [Turkish Sentiment Dataset](https://www.baskent.edu.tr/~msert/research/datasets/SentimentDatasetTR.html) | Twitter | Public | ahayran@baskent.edu.tr, msert@baskent.edu.tr |
| [Omurca, Ekinci & Türkmen, 2017](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8090212) | [Turkish Hotel Review Dataset (annotated)](http://dx.doi.org/10.13140/RG.2.2.13338.44488) | Otelpuan.com | Public | silhan@kocaeli.edu.tr ekin.ekinci@kocaeli.edu.tr hazal.turkmen@kocaeli.edu.tr |
| [Mulki, Haddad, Ali & Babaoğlu, 2018](https://doi.org/10.1109/SIU.2018.8404718) | Turkish Movie & Multidomain Product Reviews *Reused* *from [Demirtas & Pechenizkiy, (2013)](https://www.win.tue.nl/~mpechen/projects/smm/#Datasets)* | Hepsiburada.com | Public           | halamulki@selcuk.edu.tr ibaboglu@selcuk.edu.tr Hatem.Haddad@ulb.ac.be chedi.bechikh@gmail.com |
| [Yüksel & Tan, 2018](https://hrcak.srce.hr/file/328239) | [Foursquare Venue and Comments Data](https://data.mendeley.com/datasets/29tbvvwkdp/2) | Foursquare | Public | asimyuksel@sdu.edu.tr |
| [Ay Karakuş, Talo, Hallaç & Aydın, 2018](https://www.researchgate.net/profile/Betul-Ay-2/publication/326443062_Evaluating_deep_learning_models_for_sentiment_classification/links/5b5087fa0f7e9b240fede03d/Evaluating-deep-learning-models-for-sentiment-classification.pdf) | [Turkish Movie Reviews Dataset](http://buyukveri.firat.edu.tr) | Beyazperde.com | Public | betulaykarakus@gmail.com, mtalo@firat.edu.tr, irhallac@firat.edu.tr, gaydin@firat.edu.tr |
| [Yurtalan, Koyuncu & Turhan, 2019](https://journals.tubitak.gov.tr/cgi/viewcontent.cgi?article=1724&context=elektrik) | Turkish Twitter Dataset | Twitter | Not Available | mkoyuncu@atilim.edu.tr |
| [Amasyalı, Taşköprü & Çalışkan, 2018](https://doi.org/10.1109/ASYU.2018.8554037) | [Turkish Telecom Twitter Dataset](https://github.com/mfatihamasyali/sentiment_deep_or_classical) | Twitter | Public | mfatih@ce.yildiz.edu.tr, hakantaskopru77@gmail.com, kubra.clskn94@gmail.com |
| [Çiftçi & Apaydın, 2019](https://doi.org/10.1109/IDAP.2018.8620751) | Turkish Product & Movie Reviews Dataset | Hepsiburada.com & Beyazperde.com | Not Available | basri.ciftci@std.sehir.edu.tr apaydin@sehir.edu.tr |
| [Çoban & Özyer, 2018](https://doi.org/10.1109/IDAP.2018.8620757) | VS1 - [3000 Turkish Tweets](http://www.kemik.yildiz.edu.tr/data/File/3000tweet.rar), VS2 - *Reused from [Hayran & Sert (2017)](http://www.baskent.edu.tr/~msert/research/datasets/SentimentDatasetTR.html)* | Twitter | Public | ocoban@cu.edu.tr gulsah.ozyer@atauni.edu.tr |
| [Oğul & Güran, 2019](https://doi.org/10.1109/UBMK.2019.8907041) | VS1 - [SemEval-2017 Task 4](http://alt.qcri.org/semeval2017/task4/index.php?id=download-thefull-training-data-for-semeval-2017-task-4), VS2 - *Reused from [Amasyalı et al. (2018)](https://github.com/mfatihamasyali/sentiment_deep_or_classical)*, VS3 - [CrowdFlower Airline Dataset](https://www.kaggle.com/crowdflower/twitter-airline-sentiment) | Twitter | Public | 20172105039@dogus.edu.tr adogrusoz@dogus.edu.tr | 
| [Uslu, Tekin & Aytekin, 2019](https://doi.org/10.1109/SIU.2019.8806355) | VS1 - [YTÜ/Kemik Dataset](http://www.kemik.yildiz.edu.tr/) (Reused from Amasyalı et al., 2018), VS2 - Movie Comments, VS3 - Movie Comments, VS4 - Movie Comments| Beyazperde.com | Not Available | abdullah.uslu@bahcesehir.edu.tr sefa.tekin@bahcesehir.edu.tr tevfik.aytekin@eng.bau.edu.tr |
| [Akın & Yıldız, 2019](https://doi.org/10.1109/INISTA.2019.8778305) | VS1 - Restaurant Reviews, VS2 - [Product Reviews](https://github.com/fthbrmnby/turkish-text-data) | Comment | VS1: Not Available, VS2: Publicly Available | emre.akin02@bilgiedu.net tugba.yildiz@bilgi.edu.tr |
| [Santur, 2019](https://doi.org/10.1109/IDAP.2019.8875985) |[Turkish Movie Sentiment Analysis Dataset](https://www.kaggle.com/datasets/sercansantur/turkish-movie-sentiment-analysis-dataset) | E-commerce Reviews | Public | ysantur@firat.edu.tr |
| [Rumelli et al., 2019](https://ieeexplore.ieee.org/document/8945268) | Hepsiburada Product Reviews | E-commerce Reviews | Not Available | merve.rumelli@ceng.deu.edu.tr, deniz.akkus@ceng.deu.edu.tr, ozge.kart@deu.edu.tr, zerrin@cs.deu.edu.tr |
| [Shehu et al., 2019](https://watermark.silverchair.com/080004_1_online.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAyswggMnBgkqhkiG9w0BBwagggMYMIIDFAIBADCCAw0GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMOp7va0bqTkULhcO3AgEQgIIC3iq40qIR2y2ysI8UDHtKSV6WWaIWg3kckzM_CgR3XJnX_ymFSVUQGJj7UMkh-SjLRGkM0gwv8cJrnRHFFBzqMJoUA2YZELNVxwcAXnSqFgvb6rF48Ca1CQvF-opeqGI0xu2JvVc1d1vvTOEU8PzIU5OTYlC9Ukwl7cloPHqUKUqMVtCd4VoR0B3RRr3ekKTZa_vj5lTrWFuHoZkCTbLAhAL4jTUvNVp63W5Hx_anLUPGN8JMUlb3D3GSbgIWatc2zmRRHI7WQDlYYZnqq2yqdtUEYhBZ5_ziGCUCrHXLNRvyzRvJmYgqRvEQmAEN8E51bNndoeiAGvuDzpvYSwJbja4JcknCdUdFGt57boRH_VH1IPacuw3xDcPnpOl9r7-QeADttZMMKGx0fxjeolKV9FFBkxEo5S-QaQvCHqg4DJT0aRijtNb_o2jtLxxXa2esWVGAa6RshpIr7hgptfB8ycKkCY3ZqBEbaJswQ8ZuqkxrSBskKnSk7uENSv6RlrC1JRqaBMWRITjwvuIoE34oeRP4HnpOZk3h8M0ubTD1PcbBIyKzuH8YwKzg9AJVQ1XYVV5upzNXVUpK4vclfir0kFwK_zgQo0m7nsLAwhGA57VBtZFkQD3igqRfP-6DaOhAByyQY9NYvB3ONYLJRhOCbNBawxGxO5ajpBJDLUVoeCxoJdjUo-Viyv9SqYRJt12UDYh4in-WhKXyJ3l3mlNjyTx79UT0GKZxpB2NuhdYA21vm9phPg53KFft9GDlAAsapM72YIWkPh67B-b3URpHGzhjwG9no22X3ZmxcvfTn4uvkes1vIVVFEn8aaS1wGqBgB2IAJcCT50N6CApvzTdFo0P--fKlYI75QTPe79SxZgPUL2QYJZdGE2k6TQ6peNQuKw6kMpihAPQ9sXHbensvhPnIkooQv-YjtHwDoj4jKH8yGXqgWZ2zFJs7kz9ZgYHysgwvOK1LxfgouB7iOz-) | Turkish Twitter Dataset | Tweets | Not Available | harisushehu@gmail.com stokat@pau.edu.tr md.sharif@uoh.edu.sa uyaver@tau.edu.tr |
| [Erşahin et al., 2019](https://journals.tubitak.gov.tr/elektrik/vol27/iss3/16) | VS1 - [Movie Review](http://humirapps.cs.hacettepe.edu.tr/tsad.aspx) (Reused from Uçan et al., 2016), VS2 - [Hotel Review](http://humirapps.cs.hacettepe.edu.tr/tsad.aspx) (Reused from Uçan et al., 2016), VS3 - [Twitter Dataset](http://www.kemik.yildiz.edu.tr) (Reused from Amasyalı et al., 2018) | Comment & Tweet | Public | buketoksuzoglu@iyte.edu.tr hakankara@iyte.edu.tr ozge.kart@deu.edu.tr zerrin@cs.deu.edu.tr |
| [Karamollaoğlu et al., 2019](https://ieeexplore.ieee.org/document/8993416) | Dataset | Twitter | Not Public | h.karamollaoglu@euas.gov.tr iadogru@gazi.edu.tr oyildiz@gazi.edu.tr nursal@gazi.edu.tr |
| [Bayraktar, Yavuoğlu & Özbilen, 2019](https://ieeexplore.ieee.org/document/9005947) | [SemEval 2016 ABSA Turkish Restaurant Dataset](http://alt.qcri.org/semeval2016/task5/) *Reused from [Pontiki et al., (2016)](http://alt.qcri.org/semeval2016/task5/)* | Restaurant reviews (SemEval) | Public | Contains 1232 train / 144 test sentences. Used for aspect-based sentiment analysis. bayraktarkivanc@gmail.com |
| [Demirci, Keskin & Doğan, 2019](https://ieeexplore.ieee.org/document/9005952) | Twitter Dataset | Twitter | Not Available | demirci18@itu.edu.tr serefrecepkeskin@gmail.com dogang@uncw.edu|
| [Güven, Diri & Çakaloğlu, 2020](https://doi.org/10.17341/gazimmfd.556104) | [Turkish Tweets Dataset](https://www.kaggle.com/anil1055/turkish-tweet-dataset) | Twitter | Available |  zekeriya.anil.guven@ege.edu.tr diri@yildiz.edu.tr txcakaloglu@ualr.edu |
| [Shehu & Tokat, 2020](https://www.researchgate.net/publication/338362981_A_Hybrid_Approach_for_the_Sentiment_Analysis_of_Turkish_Twitter_Data) | Turkish Twitter Dataset | Twitter | Not Available | harisushehu@gmail.com, stokat@pau.edu.tr |
| [Kilimci, 2020](https://www.researchgate.net/profile/Zeynep-Kilimci/publication/338124910_Borsa_tahmini_icin_Derin_Topluluk_Modellleri_DTM_ile_finansal_duygu_analizi/links/5e0b12ba4585159aa4a70b0f/Borsa-tahmini-icin-Derin-Topluluk-Modellleri-DTM-ile-finansal-duygu-analizi.pdf) | Turkish Financial Twitter Dataset | Twitter | Not Available | hkilimci@dogus.edu.tr |
| [Kilimci, Yoruk & Akyokus, 2020](https://ieeexplore.ieee.org/document/9155261) | Turkish Mobile Game Reviews Dataset | Google Play Store | Not Available | zeynep.kilimci@kocaeli.edu.tr yoruk.h@gmail.com sakyokus@medipol.edu.tr |
| [Sigirci et al., 2020](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9219407) | Turkish Google Play Reviews Dataset | Google Play Store | Not Available | onu.sigirci@loodos.com |
| [Açıkalın, Bardak & Kutlu, 2020](https://ieeexplore.ieee.org/document/9302492) | Movie & Hotel Reviews *Reused from [Uçan et al., (2016)](http://humirapps.cs.hacettepe.edu.tr/tsad.aspx)* | Beyazperde.com, Otelpuan.com | Public | u.acikalin@etu.edu.tr |
| [Alqaraleh, 2021](https://doi.org/10.34028/18/4/7) | Turkish Movie Reviews *Reused from [Demirtas & Pechenizkiy, (2013)](https://www.win.tue.nl/~mpechen/projects/smm/#Datasets)* | Beyazperde.com | Public | saed.alqaraleh@hku.edu.tr |
| [Kılıç & Büyükeke, 2021](https://doi.org/10.1109/UBMK52708.2021.9558976) | TripAdvisor, Blog, and IMDb Turkish Reviews Datasets | TripAdvisor, Blog, IMDb | Not Available | yasir.kilic@atu.edu.tr, abuyukeke@atu.edu.tr |
| [Eker, Eker & Duru, 2021](https://ieeexplore.ieee.org/document/9558958) | [Turkish Tweets Dataset](https://www.kaggle.com/anil1055/turkish-tweet-dataset) *Reused from [Güven et al., (2020)](https://doi.org/10.17341/gazimmfd.556104)* | Twitter | Public | aysegul.eker@kocaeli.edu.tr |
| [Salur & Aydın, 2021](https://ieeexplore.ieee.org/abstract/document/9599037) | [Turkish ABSA Tourism Corpus](https://github.com/salurumut/Turkish-Aspect-Based-Sentiment-Analysis-Corpus-For-Smart-Tourism) | TripAdvisor | Public | mehmetumut.salur@gibtu.edu.tr |
| [Aydın & Güngör, 2021](https://doi.org/10.1017/S1351324920000200) | Movie Reviews *Reused from [Türkmenoğlu & Cadırci, (2014)](https://d1wqtxts1xzle7.cloudfront.net/108813139/download_jsessionid_00E6A9E756589AC939F407A7F15D5AA8-libre.pdf)*, Twitter Dataset *Reused from [Amasyalı et al., (2018)](https://github.com/mfatihamasyali/sentiment_deep_or_classical)* | Beyazperde.com, Twitter | Public | cem.aydin1@boun.edu.tr |
| [Zeybek, Koç & Seçer, 2021](https://doi.org/10.1080/23311916.2021.1893621) | [MS-TR Treebank](https://data.mendeley.com/datasets/nz7vm5rchd/1), *Built upon Turkish Sentiment Treebank (TSTB)* | Movie reviews, opinionated texts | Public | sultan.zeybek@fsm.edu.tr |
| [Shehu et al., 2021](https://doi.org/10.1109/ACCESS.2021.3071393) | Stemmed Turkish Twitter Dataset | Twitter | Available Upon Request | harisushehu@ecs.vuw.ac.nz |
| [Köksal & Özgür, 2021](https://doi.org/10.1109/SIU53274.2021.9477814) | [BounTi: Turkish Sentiment Twitter Dataset](https://github.com/boun-tabi/BounTi-Turkish-Sentiment-Analysis) | Twitter | Public | abdullatif.koksal@boun.edu.tr |
| [Kemaloğlu, Küçüksille & Özgünsür, 2021](https://doi.org/10.16984/saufenbilder.872227) | Turkish Social Media Sentiment Dataset | Twitter | Not Available | nkemaloglu@mehmetakif.edu.tr ecirkucuksille@sdu.edu.tr eozgunsur@gmail.com |
| [Aydın, Öztürk & Çiçek, 2021](https://doi.org/10.17718/tojde.961825) | Turkish ODE Twitter Dataset | Twitter | Not Available | zergul@eskisehir.edu.tr |
| [Aygün, Kaya & Kaya, 2021](https://doi.org/10.1109/JBHI.2021.3133103) | [COVID-19 Vaccine Sentiment Dataset (TR & EN)](https://github.com/IrfanAygun/Covid-19-Vaccination-Dataset-and-Sentiment-Analysis) | Twitter | Public | irfan.aygun@cbu.edu.tr |
| [Aydoğan & Kocaman, 2022](https://doi.org/10.1177/01655515221074328) | [TRSAv1: Turkish E-commerce Reviews](https://github.com/maydogan23?tab=projects) | Turkish e-commerce websites | Public | murat.aydogan@firat.edu.tr |
| [Ballı et al., 2022](https://doi.org/10.1155/2022/2455160) | [SentimentSet](https://www.kaggle.com/caglaballi/sentimentset), Public Datset *Reused from [Beyaz (2021)](https://www.kaggle.com/mrtbeyz/trke-sosyal-medya-paylam-veriseti)* | Twitter | Public | alok.mishra@himolde.no |
| [Mutlu & Özgür, 2022](https://arxiv.org/abs/2205.04185) | [Turkish Targeted Sentiment Twitter Dataset](https://github.com/melihmutlu/targeted-sentiment-analysis-turkish) | Twitter | Public (Tweet IDs) | melih.mutlu@boun.edu.tr |
| [Kabakus, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9074424/pdf/CPE-34-0.pdf) | Turkish COVID-19 Twitter Dataset | Twitter | Available Upon Request | talhakabakus@duzce.edu.tr |
| [Güven, 2022](https://doi.org/10.1145/3557892) | [TSAD: Turkish Hotel & Movie Reviews](http://humirapps.cs.hacettepe.edu.tr/tsad.aspx) *Reused from [Uçan et al., 2016]* | Beyazperde.com, Otelpuan.com | Public | anilguven1055@gmail.com |
| [Erkan & Güngör, 2023](https://doi.org/10.1109/ACCESS.2023.3337354) | [Semeval 2016 Turkish Restaurant Reviews](https://alt.qcri.org/semeval2016/task5/) *Reused from [Pontiki et al., 2016]*, [Beyazperde Movie Reviews](http://humirapps.cs.hacettepe.edu.tr/tsad.aspx) *Reused from [Uçan et al., 2016]* | Twitter, Beyazperde.com | Public | ali.erkan@boun.edu.tr  |
| [Alnahas et al., 2022](https://doi.org/10.1109/IISEC56263.2022.9998264) | Turkish E-commerce Reviews Dataset | Turkish e-commerce websites | Not Available | dalnahas@infina.com.tr |
| [Karayiğit et al., 2022](http://dx.doi.org/10.5755/j01.itc.51.3.30276) | [Turkish Instagram COVID-19 Comments Dataset](https://github.com/habibekarayigit/Turkish_Datasets) | Instagram | Public | d2014242@mersin.edu.tr |
| [Demir & Bilgin, 2023](https://doi.org/10.1109/UBMK59864.2023.10286719) | Turkish News Sentiment Dataset | Turkish news articles (source unspecified) | Not Available | engindemir@uludag.edu.tr |
| [Abdellatif et al., 2023](https://doi.org/10.1109/ICCIT58132.2023.10273894) | Turkish Twitter & Hepsiburada Dataset | Twitter, Hepsiburada.com | Not Available | atabdellatif@fsm.edu.tr |
| [Altınok, 2023](https://aclanthology.org/2023.acl-long.768) | [Beyazperde Reviews](https://github.com/turkish-nlp-suite/BeyazPerde-Movie-Reviews), [Supplements Reviews](https://github.com/turkish-nlp-suite/Vitamins-Supplements-Reviews), [Corona-mini](https://github.com/turkish-nlp-suite/Corona-mini-dataset) | Beyazperde.com, Vitaminler.com, Ekşi Sözlük | Public | duygu.altinok@deepgram.com |
| [Tohma et al., 2023](https://doi.org/10.1109/ACCESS.2023.3291592) | [DS1](https://www.kaggle.com/datasets/mesutbeyaz/turkish-social-media-comments-dataset) *Reused from [Beyaz (2021)]*, [SentimentSet](https://www.kaggle.com/datasets/ozlerhakan/twitter-sentiment-analysis-dataset) *Reused from [Özler (2021)]*, SCD (custom QA dataset) | Twitter, Social Media, QA Dialogues | 2 Public, 1 Not Available | kadir.tohma@iste.edu.tr |
| [Aydın, Güngör & Erkan, 2023](https://arxiv.org/pdf/2001.01269) | [Movie Reviews](https://github.com/cemrifki/sentiment-embeddings/tree/main/movie_reviews_dataset), [Twitter Dataset](https://github.com/cemrifki/sentiment-embeddings/tree/main/twitter_dataset) | Beyazperde.com, Twitter | Public | cemrifkiaydin@gmail.com |
| [Yılmaz & Altunay, 2023](https://doi.org/10.1016/j.teler.2023.100094) | Turkish Smartphone Reviews Dataset  | E-commerce Platforms (Trendyol, Hepsiburada, N11, GittiGidiyor, Amazon Türkiye) | Available Upon Request | mustafa.yilmaz@samsun.edu.tr halealtunay@isparta.edu.tr |
| [Ezin, Kiziltepe & Karakus, 2024](https://doi.org/10.1109/UBMK63289.2024.10773485) | [TRSAv1](https://github.com/maydogan23/TRSAv1-Dataset) *Reused from [Aydogan & Kocaman, 2023]*, [VSCR](https://github.com/turkish-nlp-suite/Vitamins-Supplements-Reviews) *Reused from [Altinok, 2023]* | E-commerce Platforms | Public | ercan.ezin@harran.edu.tr |
| [Özdemir, Giritli & Can, 2024](https://doi.org/10.1109/UBMK63289.2024.10773456) | [Turkish Hotel Reviews Dataset](https://github.com/AtaOnur/Sentimel-Analysis-Hotel-Reviews) | Booking Platforms | Public | ataonur@isik.edu.tr |
| [Kiziltepe, Ezin & Karakus, 2024](https://doi.org/10.1109/ASYU62119.2024.10757130) | [VSCR](https://github.com/turkish-nlp-suite/Vitamins-Supplements-Reviews) *Reused from [Altinok, 2023]*, [TRSAv1](https://github.com/maydogan23/TRSAv1-Dataset) *Reused from [Aydogan & Kocaman, 2023]* | E-commerce Platforms | Public | rukiye.savrankiziltepe@ktu.edu.tr |
| [Polat et al., 2024](https://doi.org/10.1109/ACCESS.2024.3496867) | Couple Dialogue Dataset | In-lab conversations (Özyeğin University) | Not Public | nafiye.polat@ozu.edu.tr |
| [Ba Alawi & Bozkurt, 2024](https://doi.org/10.1109/SIU61531.2024.10600970) | Turkish University Twitter Dataset | Twitter | Not Available | baalawi.abdulfattah@gmail.com |
| [Ba Alawi & Bozkurt, 2024](https://doi.org/10.1007/s13369-024-09360-4) | VS1 - Turkish Higher Education Dataset (THED), VS2 - *Reused from [Ucan et al. (2016)](http://humirapps.cs.hacettepe.edu.tr/tsad.aspx)* | Twitter (X), Hotel Reviews | THED: Not Public, HRD: Public | baalawi.abdulfattah@gmail.com, fbozkurt@atauni.edu.tr |
| [Nasution & Onan, 2024](https://doi.org/10.1109/ACCESS.2024.3402809) | DTC (Topic), DTSA (Sentiment), DEC (Emotion) | Newspapers, Twitter, Turkish literature | Not Public | aytug.onan@ikcu.edu.tr |
| [Onan & Balbal, 2024](https://doi.org/10.1109/ACCESS.2024.3349971) | [TRSAv1](https://github.com/maydogan23/TRSAv1-Dataset) *Reused from [Aydogan & Kocaman, 2023](https://doi.org/10.1177/01655515221074328)*, Turkish Emotions Dataset, MR (Amazon), Swahili News Dataset | E-commerce, Blogs, Amazon Reviews, News Articles | Public, Not Public | aytug.onan@ikcu.edu.tr |
| [Bozuyla, 2023](https://doi.org/10.1145/3626523) | Turkish Drug Review Dataset | eksisozluk.com, drugs.com (translated) | Not Public | mbozuyla05@posta.pau.edu.tr |
| [Cam et al., 2024](https://doi.org/10.1016/j.heliyon.2023.e23784) | Financial Turkish Twitter Dataset | Twitter (#Borsaistanbul, #Bist, #Bist30, #Bist100) | Not Public | hcam@gumushane.edu.tr |
| [Ba Alawi & Bozkurt, 2024](https://doi.org/10.1016/j.dajour.2024.100473) | Turkish Universities Twitter Dataset | Twitter | Available Upon Request | baalawi.abdulfattah@gmail.com |
| [Najafi & Varol, 2023](https://arxiv.org/abs/2311.18063) | [VRLSentiment](https://github.com/VRL-Lab/VRLSentiment), [TSATweets](https://github.com/sercankulcu/sentiment-analysis-of-tweets-in-Turkish) *Reused from Kulcu (2015)*, [Kemik-17bin](http://www.kemik.yildiz.edu.tr/veri_kumelerimiz.html) *Reused from Amasyalı et al. (2018)*, [Kemik-3000](http://www.kemik.yildiz.edu.tr/veri_kumelerimiz.html) *Reused from Amasyalı et al. (2018)*, [BOUN (BounTi)](https://github.com/boun-tabi/BounTi-Turkish-Sentiment-Analysis) *Reused from Köksal & Özgür (2021)*, [TSAD](https://huggingface.co/datasets/winvoker/turkish-sentiment-analysis-dataset) *Reused from Uçan et al. (2016)* | Twitter | Public | onur.varol@sabanciuniv.edu |
| [Zümberoğlu et al., 2025](https://doi.org/10.3390/app15042062) | [FSMTSAD](https://github.com/kevserbusrayildirim/FSMTSAD), [BOUN (BounTi)](https://github.com/boun-tabi/BounTi-Turkish-Sentiment-Analysis) *Reused from Köksal & Özgür (2021)* | Tweets, Product & Service Reviews | Public | ssahmoud@fsm.edu.tr |
| [Özmen & Gündüz, 2025](https://doi.org/10.3390/app15052297) | Turkish Cosmetic Product Reviews Dataset | E-commerce Reviews (Trendyol) | Not Public | cgokce.elkovan@hku.edu.tr sgunduz@atu.edu.tr |
| [Kaya, Fidan & Toroslu, 2012](https://doi.org/10.1109/WI-IAT.2012.115) | Turkish Political News Columns Dataset | News Columns (6 Turkish newspapers) | Not Public | mesut.kaya@agmlab.com |
| [Sağlam, Sever & Genç, 2016](https://doi.org/10.1109/SIU.2016.7495900) | SWNetTR *Reused from [Uçan, 2014](http://www.cs.hacettepe.edu.tr/lisansustu/files/aucanmaster.pdf)*, [SWNetTR-GDELT](https://www.gdeltproject.org/data.html), SWNetTR-PLUS, MLTC | News Media (GDELT), Turkish Lexicons | Public, Not Public | fsaglam@kho.edu.tr sever@hacettepe.edu.tr burkay.genc@hacettepe.edu.tr  |
| [Makinist et al., 2018](https://arxiv.org/abs/1801.09975) | Improved Turkish Movie Review Dataset | Turkish movie review website (collected via Apache MCF) | Not Public | semihamakinist@gmail.com |


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


