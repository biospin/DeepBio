# DeepBio

<img src="https://github.com/biospin/DeepBio/blob/master/main_02.jpg" width="500" height="300" />

## 스터디 정보
파이썬을 이용한 바이오인포매틱스 + 딥러닝에 대한 스터디입니다.

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
- 실습 계획 :
     - 1) 회귀모형을 활용한 모형 개발
     - 2) Multilayer Perceptron을 활용한 모형 개발
     - 3) DBN을 활용한 모형 개발
- 실습 환경 : NCloud 서버 2대와  스터디 구성원의 준비해주는 장비

| 서버명    |        서버OS |  서버 구성                             | 공인 IP
|--------|--------------|------------------------|-------------
|biospin | ubuntu 14.04 | 8CPU, 16G Mem, 50G HDD | 211.249.50.37
|darwin  | ubuntu 14.04 | 8CPU, 16G Mem, 50G HDD | 미할당


## 참고 자료
- [Bengio 교수의 딥러닝 강의]( http://goodfeli.github.io/dlbook/ ) - 딥러닝에 대한 깊은 통찰을 얻을 수 있음.
- [스탠포드대학의 Convolutional Neural Networks for Visual Recognition 강의](http://cs231n.stanford.edu/syllabus.html) - 딥러닝에 사용되는 수식을 쉽게 설명
- [Docker로 Caffe 실습하기](https://gist.github.com/haje01/0fb6d63bf065c9831256)
- [Basset-Deep convolutional neural networks for DNA sequence analysis](https://github.com/davek44/Basset)
- [남광우님의 Basset 노트 ](https://github.com/biospin/DeepBio/blob/master/reference/Basset.txt)
- [Theano의 Graph Structures예제에서 발생하는 오류 해결방법](https://github.com/biospin/DeepBio/blob/master/reference/pydot_error.txt)
- [NVIDA CUDA 드라이버설치 방법](http://docs.nvidia.com/cuda/cuda-getting-started-guide-for-linux/index.html#pre-installation-actions)
- [우분투 14.04에 NVIDA CUDA 드라이버설치 ] (https://github.com/biospin/DeepBio/blob/master/reference/00_cuda_install.ipynb)

## 스터디 공지
- [12월 08일  DeepBio:파트 2 - 2회차]( https://www.facebook.com/events/791234627652955/ )
- [12월 01일  DeepBio:파트 2 - 1회차]( https://www.facebook.com/events/899904310064718/ )
- [11월 24일  DeepBio:파트 1 - 4회차]( https://www.facebook.com/events/981481878589792/ )
- [11월 17일  DeepBio:파트 1 - 3회차]( https://www.facebook.com/events/549067748577623/ ) 
- [11월 10일  DeepBio:파트 1 - 2회차]( https://www.facebook.com/events/1677532639129156/ )

## Schedule

### Part 1.

1. 장소: 토즈 아트레온점 ( http://www.toz.co.kr/branch/main/index.htm?id=6 )
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
|    |          |(Theano) [Theano 기초 - Derivatives in Theano](https://github.com/biospin/DeepBio/blob/master/part02/Week1_151201/Derivates20in20Theano.ipynb%) (박혜진)
|  2 |2015/12/08|(파이션 기초) 14장 데이터베이스와 SQL, 15장 데이터 시각화와 16장 (이승현)
|    |          |(Theano) Theano 기초 -  Configuration Settings and Compiling Modes 와 Loading and Saving(성민경)
|  3 |2015/12/15|(bioPython ) 1장: Python and the Surrounding Software Ecology 
|    |          |(Theano) Theano 기초 - Conditions과 Loop
|    |          |(특강)[우분투에 CUDA 설치](https://github.com/biospin/DeepBio/blob/master/reference/00_cuda_install.ipynb) (지용기)
|  4 |2015/12/22|(bioPython ) 2장: Next-generation Sequencing 
|    |          |(Theano) Theano 기초 - Sparse 과 Using the GPU (김가경)


### Part 3.
|seq.| 날 짜           |내용
|----| ---------|----------------------------------------------
|  1 |2015/12/29|(bioPython )   3장: Working with Genomes 
|    |          |(Theano)  Deeplearning  - 3장 GETTING STARTED 
|  2 |2016/01/05|(bioPython ) 4장: Population Genetics 
|    |          |(Theano)  Deeplearning  - 4장 Classifying MNIST digits using Logistic Regression  
|    |          |(실습) [암 환자 RNA정보를 활용한 암 예측 모델 개발 - 암환자 RNA 정보 획득방법 및 Data 구조파악](https://github.com/biospin/DeepBio/blob/master/part03/Week1_160105/Cancer_Data.ipynb) 
|  3 |2016/01/12|(bioPython )   5장: Population Genetics Simulation (Theano) 5장 Multilayer Perceptron  이론  
|    |          |(Theano) 5장 Multilayer Perceptron  코드설명 및 실습   
|    |          |(실습) 암 환자 RNA정보를 활용한 암 예측 모델 개발 - Data 전처리
|  4 |2016/01/19|(bioPython ) 6장: Phylogenetics (Theano) 6장 Convolutional Neural Networks (LeNet)  이론 
|    |          |(Theano) 6장 Convolutional Neural Networks (LeNet)  코드설명 및 실습   
|    |          |(실습) 암 환자 RNA정보를 활용한 암 예측 모델 개발 - 회귀모형을 활용한 모형 개발

 