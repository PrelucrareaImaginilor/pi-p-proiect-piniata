# Clasificarea medicamentelor
## Introducere
Apariția a tot mai multor medicamente a dus la cosumarea în necunoștință a acestora. Pentru evitarea acestui lucru se încearcă crearea de aplicații și moduri de recunoaștere a pastilelor în moduri ușor de folosit de toată lumea, iar acestea reprezintă unul din motivele pentru care clasificarea medicamentelor reprezintă un domeniu de interes Scopul nostru este de a identifica pastilele primite ca input, prin clasificarea acestora în funcție de culoare și formă.
## Metoda de rezolvare abordată
Pentru realizarea proiectului am utilizat Python 3.8.20 cu librăriile: OpenCV, TensorFlow, Matplotlib, Pandas și PIL.
Detectarea <b>formelor</b> medicamentelor a fost făcută prin preluarea unei singure pastile din imaginea inițială, aplicarea unu filtru bilateral pentru netezirea imaginii fără a estompa muchiile și aplicarea algoritmului de detectie a muchiilor Canny, imaginea prelucrată va fi preluată de o rețea neuronală convoluțională.

<!--aici de pus o poza-->
<div align="center">
    <img src=/results/shape_canny.png>
</div>
<p>
Pentru detectarea <b>culorilor</b> am utilizat un filtru median de netezire. Mai apoi am folosit media culorilor din doua zone de interes din imagine pentru a obține valorile RGB. Acestea sunt preluate de o rețea neuronală multilayer care va numi culorile date.
</p>
<div align=center>
          <img src=/results/color_nn.png> 

</div>

## Rezultate
•	Printr-o trecere de la abordare  manuală  de împărțire a spațiului HSV la o rețea neuronală s-a constat o creștere a acurateții de 15%.
•	Prin schimbarea metodei de preprocesare a imaginii pentru detecția formei s-a constat o creștere a acurateții de 4%.
<div align=center>
  <img src=/results/shape_color_ac.png>
  <img src=/results/shape_ac.png>
  <img src=/results/color_ac.png>
</div>

## Limitări 
   Limitările vin de la setul de date care anumite culori etichetate greșit, dificultatea  extragerii textului cauzată de gravura în pastilă și de rezoluția imaginilor, și distribuție inegală a formelor/culorilor în datele de test și cele de antrenare.
  
## Bibliografie
1.Dataset: https://healthdata.gov/w/5vhs-kfa6/default?cur=0pRtVXYvSWA <br>
2.<a href=https://www.tensorflow.org/api_docs>TensorFlow</a> <br>
3.<a href=https://docs.opencv.org/4.x/index.html
     >OpenCV</a><br>
4.<a href=https://ieeexplore.ieee.org/abstract/document/8923984>Pill Image Classification using Machine Learning - Luan Sousa Cordeiro, Joyce Saraiva Lima, A. Iedo Rocha Ribeiro, Francisco Nivando Bezerra, Pedro P. Rebouças Filho, Ajalmar R. Rocha Neto</a><br>
5.<a href=https://ieeexplore.ieee.org/abstract/document/8939727/authors#authors>MobilePill: Accurate Pill Image Classification via Deep Learning on Mobile - Asif Mehmood, Chaehoon Yoon, Seungjae Kim, Sungjin Kim</a><br>
6.<a href=https://ieeexplore.ieee.org/document/8937272>Preliminary Study of Multi Convolution Neural Network-Based Model To Identify Pills Image Using Classification Rules - Narasak Boonthep, Jirabhorn Chaiwongsai, Bowonsak Srisungsittisunti, Thana Udomsripaiboon</a><br>
7.<a href=https://www.mdpi.com/2076-3417/14/19/9065>Combination Pattern Method Using Deep Learning for Pill Classification - Svetlana Kim, Eun-Young Park, Jun-Seok Kim 3 andSun-Young Ihm </a> <br>
8.<a href=https://ieeexplore.ieee.org/document/10479992>Drug image classification with deep learning by using Fast Region-based Convolution Neural Network - Narasak Boonthep, Jirabhorn Chaiwongsai,Bowonsak Srisungsittisunti, Thana Udomsripaiboon</a>
