<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Sentiment Analysis using Vader for Customer Review</h3>

  <p align="center">
    <a href="https://github.com/khawslee/case-study-comparative-study/blob/main/Sentiment%20Analysis%20Using%20Vader%20for%20Customer%20Review.pdf"><strong>Explore the paper »</strong></a>
    <br />
    <br />
    <a href="https://github.com/khawslee/Sentiment-Analysis-Using-Vader">View Demo</a>
    ·
    <a href="https://github.com/khawslee/Sentiment-Analysis-Using-Vader/issues">Report Bug</a>
    ·
    <a href="https://github.com/khawslee/Sentiment-Analysis-Using-Vader/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Opinions and reviews are a central part of all human activities and it’s the key influencers of our behaviors. This project focuses on the opinion
mining of customers by classifying the polarity of reviews in terms of positive (good), negative (bad), and neutral. It is important to capture the public opinion on products and services to strengthen customer support. Manual labeling of each review by humans is time-consuming and error prompting.

This project used python library's VADER sentiment to label the reviews to provide fast insight into product option trends.

<p align="right">(<a href="#top">back to top</a>)</p>

### Python library

List of python's library used in the project,

* [VaderSentiment 3.3.2](https://pypi.org/project/vaderSentiment/)
* [Pandas](https://pypi.org/project/pandas/)
* [Sklearn](https://pypi.org/project/scikit-learn/)
* [Seaborn](https://pypi.org/project/seaborn/)
* [Matplotlib](https://matplotlib.org/)
* [Numpy](https://pypi.org/project/numpy/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You are required to install vaderSentiment library before running jupyter notebook script.

* vaderSentiment
  ```sh
  pip install vaderSentiment
  ```

## Usage

VaderSentiment is both a qualitative and quantitative method that empirically validates the fold standard sentiment lexicon. It does not require any training data, supports emoticons, works in an adverse domain, and has a relatively good speed performance.

The polarity score return by analyser.polarity_scores() reflect the sentiment of the text input, polarity score of > 0.05 is consider positive, < -0.05 is consider as negative and score between -0.05 to 0.05 is neutral sentiment.

_For literature paper, please refer to the [Documentation](https://github.com/khawslee/case-study-comparative-study/blob/main/Sentiment%20Analysis%20Using%20Vader%20for%20Customer%20Review.pdf)_

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - Siang Lee, Khaw - khawslee@gmail.com

Project Link: [https://github.com/khawslee/Sentiment-Analysis-Using-Vader](https://github.com/khawslee/Sentiment-Analysis-Using-Vader)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Thangeswariy Ramanei

<p align="right">(<a href="#top">back to top</a>)</p>


[contributors-shield]: https://img.shields.io/github/contributors/khawslee/Sentiment-Analysis-Using-Vader.svg?style=for-the-badge
[contributors-url]: https://github.com/khawslee/Sentiment-Analysis-Using-Vader/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/khawslee/Sentiment-Analysis-Using-Vader.svg?style=for-the-badge
[forks-url]: https://github.com/khawslee/Sentiment-Analysis-Using-Vader/network/members
[stars-shield]: https://img.shields.io/github/stars/khawslee/Sentiment-Analysis-Using-Vader.svg?style=for-the-badge
[stars-url]: https://github.com/khawslee/Sentiment-Analysis-Using-Vader/stargazers
[issues-shield]: https://img.shields.io/github/issues/khawslee/Sentiment-Analysis-Using-Vader.svg?style=for-the-badge
[issues-url]: https://github.com/khawslee/Sentiment-Analysis-Using-Vader/issues
[license-shield]: https://img.shields.io/github/license/khawslee/Sentiment-Analysis-Using-Vader.svg?style=for-the-badge
[license-url]: https://github.com/khawslee/Sentiment-Analysis-Using-Vader/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/khawslee
