# MediLab
## An AI soluton for diagnosis of Pulmonary Tuberculosis

![Medilab Website](https://github.com/chetanpandey1266/HackInIndia/blob/master/medilab.gif)

### Why we need such solution

About a third of the world’s population is infected with Mycobacterium tuberculosis. Among communicable diseases, TB is the second leading cause of death worldwide after HIV/AIDS, killing nearly 2 million people each year. More than a half of TB cases occur in the largest Asian countries (India, China, Indonesia, Bangladesh, Philippines, and Pakistan).

India accounts for one fourth of the global TB burden. In 2015, an estimated 28 lakh cases occurred and 4.8 lakh people died due to TB. India has highest burden of both TB and MDR TB based on estimates reported in Global TB Report 2016. About 85% of the all cases in India are of pulmonary tuberculosis.

### Our Solution
Our AI solution aims at helping people diagnosis their Tuberculosis faster than before so that they could get proper treatment at an early stage. We provide a deep learning based backend with an easy to use frontend(webapp) which can be used by hospitals/pathologies to diagnosis their patients. In backend we will be running a python script with our pretrained model that would return the probability whether a patient is suffering from the disease or not.

We have used fastai, an easy to use ML package based build over Pytorch, to train our model. We have used trained pretrained resnet34 model and got an accuracy close to 90 percent

### Our FrontEnd

#### Our Home Page
![Image01](https://github.com/chetanpandey1266/HackInIndia/blob/master/images/01.png)
An attractive homepage developed completely using HTML, CSS, Bootstrap and Javascript

#### Login Page
![Image02](https://github.com/chetanpandey1266/HackInIndia/blob/master/images/02.png)
User can login to use our AI system 

#### Frequently Asked Question Section
![Image03](https://github.com/chetanpandey1266/HackInIndia/blob/master/images/03.png)
A FAQ section to help user better understand our product
# Diagnosing-TB
Using Neural Networks on Chest Xrays to find abnormal and normal xrays to diagnose for Pulmonary Tuberculosis

## Dataset
The Dataset was taken from two sources.
Then CNN was applied to a combination of 2 datasets.

### China Set
The standard digital image database for Tuberculosis is created by the National Library of Medicine, Maryland, USA in collaboration with Shenzhen No.3 People’s Hospital, Guangdong Medical College, Shenzhen, China. The Chest X-rays are from out-patient clinics, and were captured as part of the daily routine using Philips DR Digital Diagnose systems. Number of X-rays:

336 cases with manifestation of tuberculosis, and
326 normal cases.
It is requested that publications resulting from the use of this data attribute the source (National Library of Medicine, National Institutes of Health, Bethesda, MD, USA and Shenzhen No.3 People’s Hospital, Guangdong Medical College, Shenzhen, China) and cite the following publications:

Jaeger S, Karargyris A, Candemir S, Folio L, Siegelman J, Callaghan F, Xue Z, Palaniappan K, Singh RK, Antani S, Thoma G, Wang YX, Lu PX, McDonald CJ. Automatic tuberculosis screening using chest radiographs. IEEE Trans Med Imaging. 2014 Feb;33(2):233-45. doi: 10.1109/TMI.2013.2284099. PMID: 24108713
Candemir S, Jaeger S, Palaniappan K, Musco JP, Singh RK, Xue Z, Karargyris A, Antani S, Thoma G, McDonald CJ. Lung segmentation in chest radiographs using anatomical atlases with nonrigid registration. IEEE Trans Med Imaging. 2014 Feb;33(2):577-90. doi: 10.1109/TMI.2013.2290491. PMID: 24239990
### Montogomery County Set
X-ray images in this data set have been acquired from the tuberculosis control program of the Department of Health and Human Services of Montgomery County, MD, USA. This set contains 138 posterior-anterior x-rays, of which 80 x-rays are normal and 58 x-rays are abnormal with manifestations of tuberculosis. All images are de-identified and available in DICOM format. The set covers a wide range of abnormalities, including effusions and miliary patterns. The data set includes radiology readings available as a text file.

## Running
1. The IPython notebooks were trained on Google Colab with GPU(Tesla K80) enabled. The trained models have not been uploaded on to Github.
2. 640 images were used to train, and 160 to validate the results

