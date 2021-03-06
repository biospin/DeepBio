# DeepBio

<img src="https://github.com/biospin/DeepBio/blob/master/main_04.jpg" width="500" height="300" />

## 스터디 정보
파이썬을 이용한 바이오인포매틱스 + 딥러닝에 대한 스터디입니다

## 공유폴더 
https://drive.google.com/drive/folders/0B6bSLTlVnagfQ1ozTnV0anRqQWc

## 교재 정보
- 파이션 기초 - 정보교육을 위한 파이썬 (  http://python.xwmooc.org/  )
- bioPython 교재 - Bioinformatics with Python Cookbook ( http://www.amazon.com/gp/aw/d/1782175113 )
- Theano 교재 1 -  Theano 기초 ( http://deeplearning.net/software/theano/tutorial/ )
- Theano 교재 2 -  Deeplearning ( http://deeplearning.net/tutorial/deeplearning.pdf  )

## 데이터 분석 실습
- 실습 주제 : 암 환자 RNA정보를 활용한 암 예측 모델 개발
- [암환자 RNA 정보 획득방법 및 Data 구조파악](https://github.com/biospin/DeepBio/blob/master/part03/Week1_160105/Cancer_Data.ipynb)
- [암환자  mRNA 데이터 수집 및 구조](https://github.com/biospin/DeepBio/blob/master/exercise01/cancer_data_structur.ipynb)
- [암환자  mRNA데이터를 DB와 HBase에 올리기](https://github.com/biospin/DeepBio/blob/master/exercise01/mRNA_Upload_script.ipynb)
- [암환자  mRNA에서 학습용, Valiaiotion용, Test용 데이터 만들기](https://github.com/biospin/DeepBio/blob/master/exercise01/mRNA_make_feature.ipynb)
- 실습 계획 :
     - 1) 회귀모형을 활용한 모형 개발
     - 2) Multilayer Perceptron을 활용한 모형 개발
     - 3) DBN을 활용한 모형 개발
- 실습 환경 : NCloud 서버 4대와  스터디 구성원의 준비해주는 장비

| 서버명        |        서버OS |  서버 구성                               | 공인 IP          | PORT 영역
|--------  |--------------|-------------------------|-----------------|-----------------
|biospin   | ubuntu 14.04 | 8CPU, 16G Mem, 500G HDD | 211.249.50.37   | 1xxxx, 예) 18888 
|darwin    | ubuntu 14.04 | 8CPU, 16G Mem, 500G HDD | 211.249.50.37   | 2xxxx, 예) 28888
|babelpish | ubuntu 14.04 | 4CPU, 16G Mem, 500G HDD | 211.249.50.159  | 3xxxx, 예) 38888
|psygrammer| ubuntu 14.04 | 4CPU, 16G Mem, 500G HDD | 211.249.50.159  | 4xxxx, 예) 48888


| S/W                                  |  node01(darwin) |  node02(biospin) |  node03(babelpish) |  node04(psygrammer) 
|--------------------------------------|-----------------|------------------|--------------------|---------
|[Hadoop2.6](http://hadoop.apache.org/)| NameNode        | NodeManager      | NodeManager        | NodeManager
|                                      | DataNode        | DataNode         | DataNode           | DataNode
|                                      | ResourceManager |                  |                    |
|                                      |SecondaryNameNode|                  |                    |
|[Hbase1.1.2](http://hbase.apache.org/)|                 |                  | HMaster            |
|                                      |                 |                  | HRegionServer      | HRegionServer
|[Zookeeper](http://zookeeper.apache.org/)|              |                  |                    | QuorumPeerMain
|[Spark 1.5](http://spark.apache.org/) |                 | Master           |                    |
|                                      | Worker          | Worker           | Worker             | Worker
|[MariaDB](https://mariadb.com/)       |                 | mysqld           |                    |


## 참고 자료
- [Bengio 교수의 딥러닝 강의]( http://www.deeplearningbook.org/ ) - 딥러닝에 대한 깊은 통찰을 얻을 수 있음.
- [스탠포드대학의 Convolutional Neural Networks for Visual Recognition 강의](http://cs231n.stanford.edu/syllabus.html) - 딥러닝에 사용되는 수식을 쉽게 설명
- [Docker로 Caffe 실습하기](https://gist.github.com/haje01/0fb6d63bf065c9831256)
- [Basset-Deep convolutional neural networks for DNA sequence analysis](https://github.com/davek44/Basset)
- [남광우님의 Basset 노트 ](https://github.com/biospin/DeepBio/blob/master/reference/Basset.txt)
- [Theano의 Graph Structures예제에서 발생하는 오류 해결방법](https://github.com/biospin/DeepBio/blob/master/reference/pydot_error.txt)
- [NVIDA CUDA 드라이버설치 방법](http://docs.nvidia.com/cuda/cuda-getting-started-guide-for-linux/index.html#pre-installation-actions)
- [우분투 14.04에 NVIDA CUDA 드라이버설치 ] (https://github.com/biospin/DeepBio/blob/master/reference/00_cuda_install.ipynb)
- [손고리즘ML 발표자료](http://songorithm.github.io/ML/SCHEDULE/ )
- [인공신경망과 딥러닝 무료 강좌 한글](http://cyber.dbguide.net/lecture.php?action=view&no=156)
- [udacity의 Deep Learning강좌 영어](https://www.udacity.com/course/deep-learning--ud730)

## 스터디 공지
- [02월 23일  DeepBio:파트 4 - 3회차]( https://www.facebook.com/events/1246827951997544/ )
- [02월 16일  DeepBio:파트 4 - 2회차]( https://www.facebook.com/events/1020157038021388/ )
- [02월 02일  DeepBio:파트 4 - 1회차]( https://www.facebook.com/events/1672893513000173/ )
- [01월 26일  DeepBio:파트 3 - 4회차]( https://www.facebook.com/events/1542666906046268/ )
- [01월 19일  DeepBio:파트 3 - 3회차]( https://www.facebook.com/events/1086735191344745/ )
- [01월 12일  DeepBio:파트 3 - 2회차]( https://www.facebook.com/events/1543658639277708/ )
- [01월 05일  DeepBio:파트 3 - 1회차]( https://www.facebook.com/events/936812833074514/ )
- [12월 29일  DeepBio:파트 2 - 4회차]( https://www.facebook.com/events/933396823412578/ )
- [12월 15일  DeepBio:파트 2 - 3회차]( https://www.facebook.com/events/800304630099060/ )
- [12월 08일  DeepBio:파트 2 - 2회차]( https://www.facebook.com/events/791234627652955/ )
- [12월 01일  DeepBio:파트 2 - 1회차]( https://www.facebook.com/events/899904310064718/ )
- [11월 24일  DeepBio:파트 1 - 4회차]( https://www.facebook.com/events/981481878589792/ )
- [11월 17일  DeepBio:파트 1 - 3회차]( https://www.facebook.com/events/549067748577623/ ) 
- [11월 10일  DeepBio:파트 1 - 2회차]( https://www.facebook.com/events/1677532639129156/ )

## Schedule

### Part 1.

1. 장소: 토즈 신촌본점 ( http://www.toz.co.kr/branch/main/index.htm?id=5 )
2. 매주 화요일, 저녁 7시 30분~10시
3. 시작: 2015년11월 3일



|seq.|    날짜      |내용                                                                                     | 후기
|----| ---------|----------------------------------------------|-----
|  1 |2015/11/03|오리엔테이션( 김무성 )                            | [남광우님] (https://www.facebook.com/groups/biospin/permalink/770735179703033/)  
|    |          |[ (가상머신)우분투 OS에서 BioPython과 Theano 설치](https://github.com/biospin/DeepBio/blob/master/part01/Week1_151103/BioPython%EA%B3%BCTheano%EC%84%A4%EC%B9%98.txt) ( 지용기) | [먹방사진](https://www.facebook.com/groups/biospin/permalink/770110696432148/)
|    |          |[(Docker)Mac에서 BioPython과 Theano 설치](https://docs.google.com/presentation/d/1aigPAqOuY7x2X8sJ0h-I3UQVx7vFaDzye9apPYrSB7k/pub?start=true&loop=false&delayms=3000&slide=id.g7289f31dd_0_121) (박세진)    
|  2 |2015/11/10|(파이션 기초)  [2장 변수,표현식,문장  와  3장 조건부실행](https://drive.google.com/folderview?id=0B7X1ycQalUnyQW9ielhvVG1uMm8&usp=sharing&tid=0B7X1ycQalUnyWXg2MVhTbEZFT28) (안효준) |   [김강용님](https://www.facebook.com/kmirmir/posts/908489919200033)
|    |          | [연습문제풀이](https://github.com/biospin/DeepBio/blob/master/part01/Week1_151110/02%EC%9E%A5%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C.ipynb) 
|    |          | [(Theano)  Theano 기초 - NumPy refresher과 Baby Steps - Algebra](https://github.com/biospin/DeepBio/blob/master/part01/Week1_151110/DeepBio_Theano_sejinpark.ipynb)(박세진) | [김가경님](https://www.facebook.com/groups/biospin/permalink/772727886170429/) 
|  3 |2015/11/17|(파이션 기초) [4장 함수, 5장,  6장 문자열](https://drive.google.com/folderview?id=0B7X1ycQalUnyQW9ielhvVG1uMm8&usp=sharing&tid=0B7X1ycQalUnyWXg2MVhTbEZFT28)(이찬희), 7장 파일(조익연)
|    |          | [5장연습문제](https://github.com/biospin/DeepBio/blob/master/part01/Week1_151117/5%EC%9E%A5%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C.ipynb)  [6장연습문제](https://github.com/biospin/DeepBio/blob/master/part01/Week1_151117/chap06_study.ipynb) [7장연습문제](https://github.com/biospin/DeepBio/blob/master/part01/Week1_151117/chap07_file_study.ipynb) 
|    |          | (Theano)  [ Theano 기초 - More Examples](http://deeplearning.net/software/theano/tutorial/examples.html)(안효준) |   [김가경님](https://www.facebook.com/groups/biospin/permalink/772727886170429/)
|   4|2015/11/24|(파이션 기초)  [8장 리스트](https://github.com/biospin/DeepBio/blob/master/part01/Week1_151124/Py4Inf-08-Lists.pptx) 와 [9장 딕셔너리](https://github.com/biospin/DeepBio/blob/master/part01/Week1_151124/Py4Inf-09-Dictionaries.pptx) (김미송), [10장 튜플(성민경) ]  (https://github.com/biospin/DeepBio/blob/master/part01/Week1_151117/chap10_Tuple_study.ipynb) | [뒷풀이](https://www.facebook.com/groups/biospin/permalink/778259472283937/)
|    |          | [9장 연습문제](https://github.com/biospin/DeepBio/blob/master/part01/Week1_151124/chapter_09_dictionary_exercise.ipynb) |  [김가경님](https://www.facebook.com/groups/biospin/permalink/778073592302525/)
|    |          | (Theano)  Theano 기초 - [Graph Structures](http://deeplearning.net/software/theano/tutorial/symbolic_graphs.html)과 [Printing/Drawing Theano graphs](http://deeplearning.net/software/theano/tutorial/printing_drawing.html)(최홍용) 
|    |          | (보강) [ Theano 기초 - More Examples](https://github.com/biospin/DeepBio/blob/master/reference/theano_more_examples.ipynb)(지용기) | 


### Part 2.
|seq.| 날 짜           |내용                                                                                     | 후기
|----| ---------|----------------------------------------------|-----
|  1 |2015/12/01|(파이션 기초) [11장 정규표현식](https://github.com/biospin/DeepBio/blob/master/part02/Week1_151201/Regular%20expression.ipynb), [12장 네트워크 프로그램](https://github.com/biospin/DeepBio/blob/master/part02/Week1_151201/Network.ipynb)과 13장 웹서비스(김슬기) | [후기&뒷풀이](https://www.facebook.com/groups/biospin/permalink/780804322029452/)
|    |          | [11장 연습문제] (https://github.com/biospin/DeepBio/blob/master/part02/Week1_151201/11%EC%9E%A5%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C.ipynb)
|    |          |(Theano) [Theano 기초 - Derivatives in Theano](https://github.com/biospin/DeepBio/blob/master/part02/Week1_151201/Derivates%20in%20Theano.ipynb) (박혜진)
|  2 |2015/12/08|(파이션 기초) 14장 [데이터베이스와 SQL](Py4Inf-14-Databases.pptx), [Relational Databases](https://github.com/biospin/DeepBio/blob/master/part02/Week2_151208/Py4Inf-14-Database.ppt), [15장 데이터 시각화](https://github.com/biospin/DeepBio/blob/master/part02/Week2_151208/Py4Inf-15-Data-Viz.pptx)와 16장  (이승현) | [후기](https://www.facebook.com/groups/biospin/permalink/784170075026210/)
|    |          |(Theano) Theano 기초 - [Configuration Settings and Compiling Modes](https://github.com/biospin/DeepBio/blob/master/part02/Week2_151208/theano_05_configureation%20settings%20and%20compiling%20modes.ipynb) 와 [Loading and Saving](https://github.com/biospin/DeepBio/blob/master/part02/Week2_151208/theano_06_loading%20and%20saving.ipynb)(성민경)
|  3 |2015/12/15|(bioPython ) 1장: [Python and the Surrounding Software Ecology](https://github.com/biospin/DeepBio/blob/master/part02/Week3_151215/Chapter1.Python_and_the_Surrounding_Software_Ecology.ipynb), [Interface R](https://github.com/biospin/DeepBio/blob/master/part02/Week3_151215/Interfacing_R.ipynb), [R Magic](https://github.com/biospin/DeepBio/blob/master/part02/Week3_151215/R_magic.ipynb) (김가경) 
|    |          |(Theano) [Theano 기초 - Conditions과 Loop](https://github.com/biospin/DeepBio/blob/master/part02/Week3_151215/theano_loop_kang_ik_cho.pdf), [inotebook](https://github.com/biospin/DeepBio/blob/master/part02/Week3_151215/theano_loop_kang_ik_cho.ipynb) (조강익)
|    |          |(특강)[우분투에 CUDA 설치](https://github.com/biospin/DeepBio/blob/master/reference/00_cuda_install.ipynb) (지용기)
|  4 |2015/12/29|(bioPython )[ 2장: Next-generation Sequencing](https://github.com/biospin/DeepBio/blob/master/part02/Week4_151229/biopython_ch02/Chapter%202.%20Next-generation%20Sequencing.ipynb) (김가경) | [후기](https://www.facebook.com/groups/biospin/permalink/794406297335921/)
|    |          |(Theano) [Theano 기초 - Sparse 과 Using the GPU](https://github.com/biospin/DeepBio/blob/master/part02/Week4_151229/theano_%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_sparse%26GPU.pdf) (문명진)
|    |          |(논문리뷰) [Assessing the clinical utility of cancer genomic and proteomic data across tumor types](https://github.com/biospin/DeepBio/blob/master/part02/Week4_151229/paper_review/Assessing%20the%20clinical%20utility%20of%20cancer%20genomic%20and%20proteomic%20data%20across%20tumor%20types.ipynb), [논문코드 실습](https://github.com/biospin/DeepBio/blob/master/part02/Week4_151229/analysis%20code.ipynb)(성민경)


### Part 3.
|seq.| 날 짜           |내용                                                                                     | 후기
|----| ---------|----------------------------------------------|-----
|  1 |2016/01/05|(bioPython )   [3장: Working with Genomes](https://github.com/biospin/DeepBio/tree/master/part03/Week1_160105/biopython_ch03) (박혜진) | [후기](https://www.facebook.com/groups/biospin/permalink/797665063676711/)
|    |          |(Theano)  Deeplearning  - [3장 GETTING STARTED](http://www.deeplearning.net/tutorial/gettingstarted.html), [4장 Classifying MNIST digits using Logistic Regression](http://www.deeplearning.net/tutorial/logreg.html) (이승우)
|  2 |2016/01/12|(bioPython ) [4장: Population Genetics](https://github.com/biospin/DeepBio/tree/master/part03/Week2_160112/biopython04) (성민경) | [후기](https://www.facebook.com/groups/biospin/801156173327600/)
|    |          |(보강) 회귀분석 기초 (김가경)  
|    |          |(실습) [암 환자 RNA정보를 활용한 암 예측 모델 개발 - 암환자 RNA 정보 획득방법 및 Data 구조파악](https://github.com/biospin/DeepBio/blob/master/part03/Week1_160105/Cancer_Data.ipynb) 
|  3 |2016/01/19|(bioPython )   [5장: Population Genetics Simulation](https://github.com/biospin/DeepBio/tree/master/part03/Week2_160119/04_PopSim) (이승현)| [후기](https://www.facebook.com/groups/biospin/permalink/804263823016835/)
|    |          |(Theano) [5장 Multilayer Perceptron  이론   (박혜진)](https://github.com/biospin/DeepBio/blob/master/part03/Week2_160119/MLP/chap4.pdf)
|    |          |(Theano) [5장 Multilayer Perceptron  코드설명 및 실습](https://github.com/biospin/DeepBio/blob/master/part03/Week2_160119/MLP/MLP_cede.ipynb)   
|    |          |(실습) [암 환자 RNA정보를 활용한 암 예측 모델 개발 - Data 전처리(지용기)](https://github.com/biospin/DeepBio/blob/master/exercise01/mRNA_make_feature.ipynb)
|  4 |2016/01/26|(bioPython ) 6장: Phylogenetics (류재면)| [후기](https://www.facebook.com/groups/biospin/permalink/807569982686219/)
|    |          |(Theano) [6장 Convolutional Neural Networks (LeNet)  이론1](https://github.com/biospin/DeepBio/blob/master/part03/Week4_160126/CNN%20%EC%9D%B4%EB%A1%A0%20I_Final.pptx), [CNN 이론2(황성원)](https://github.com/biospin/DeepBio/blob/master/part03/Week4_160126/CNN%20%EC%9D%B4%EB%A1%A0%20II_Final.pptx)
|    |          |(Theano) [6장 Convolutional Neural Networks (LeNet)  코드설명 및 실습](https://github.com/biospin/DeepBio/blob/master/part03/Week4_160126/CNN%20%EC%BD%94%EB%93%9C%20in%20Theano_Final.pptx)   
|    |          |(보강) [Tensor (황성원)](https://github.com/biospin/DeepBio/blob/master/part03/Week4_160126/Tensor%20%EA%B8%B0%EC%B4%88_Final.pptx)
|    |          |(보강) [Tensor 참고자료](https://github.com/biospin/DeepBio/blob/master/part03/Week4_160126/Tensor%20%EC%B0%B8%EA%B3%A0%20%EC%9E%90%EB%A3%8C.PDF)
|    |          |(실습) [암 환자 RNA정보를 활용한 암 예측 모델 개발 - 회귀모형을 활용한 모형 개발(박혜진)](https://github.com/biospin/DeepBio/blob/master/exercise01/logisticRegression.py)


### Part 4.
|seq.| 날 짜           |내용
|----| ---------|----------------------------------------------
|  1 |2016/02/02|(bioPython) [7장: Using the Protein Data Bank](https://github.com/biospin/DeepBio/tree/master/part04/Week1_160202/biopython_pdb)(박혜진)
|    |          |(Theano) [ 7장 Denoising Autoencoders (dA) ](https://github.com/biospin/DeepBio/blob/master/part04/Week1_160202/DenoisingAutoencoders.ipynb)  이론(지용기)
|    |          |(Theano) 7장 Denoising Autoencoders (dA)  코드설명 및 실습 
|    |          |(실습) 암 환자 RNA정보를 활용한 암 예측 모델 개발 - Multilayer Perceptron을 활용한 모형 개발 (1)(박혜진)
|  2 |2016/02/16|(bioPython)8장: Other Topics in Bioinformatics
|    |          |(Theano) 8장 Stacked Denoising Autoencoders (SdA)  이론(김가경)
|    |          |(Theano) 8장 Stacked Denoising Autoencoders (SdA)  코드설명 및 실습 
|    |          |(실습) 암 환자 RNA정보를 활용한 암 예측 모델 개발 - Multilayer Perceptron을 활용한 모형 개발 (2)(박혜진)
|  3 |2016/02/23|(Theano) [9장 Restricted Boltzmann Machines (RBM)  이론](https://github.com/biospin/DeepBio/blob/master/part04/Week3_160223/RBM%20%EC%9D%B4%EB%A1%A0_Final_Final.pptx)(황성원)|(발표사진)(https://www.facebook.com/groups/biospin/permalink/821958491247368/)
|    |          |(Theano) 10장 Deep Belief Networks  실습 (성민경)|(후기)[https://www.facebook.com/groups/biospin/permalink/821976931245524/] 
|    |          |(실습) 암 환자 RNA정보를 활용한 암 예측 모델 개발 - DBN을 활용한 모형 개발 (2)(성민경)



  