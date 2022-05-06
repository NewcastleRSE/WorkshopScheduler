---
title: "Workshop Scheduler"
keywords: homepage
tags: [homepage]
sidebar: mydoc_sidebar
permalink: index
summary: These brief instructions will help you get started quickly with the theme. The other topics in this help provide additional information and detail about working with other aspects of this theme and Jekyll.
---

## About

When organising a Carpentries workshop a website is created for the workshop using the Carpentries workshop template (https://github.com/carpentries/workshop-template). The workshop template includes a schedule which shows the start and end times of each episode for every day including break times. This program allows a user to capture the start time of a session and the length (in minutes) of all the episodes. The program also allows break and lunch times to be inserted at any point. The program provides for initial keybard input or input from a csv file. Once the user is happy with the schedule it can be exported as an html table which can then be included in the workshop website repository saved as a file called  schedule.html.

### Project Team
Dr Jannetta Steyn ([jannetta.steyn@newcastle.ac.uk](mailto:jannetta.steyn@newcastle.ac.uk))  
Danny Watson ([https://github.com/dkwdaft/])
### RSE Contact
Jannetta Steyn
RSE Team  
Newcastle University  
([jannetta.steyn@newcastle.ac.uk](mailto:jannetta.steyn@newcastle.ac.uk))  

## Built With

- [Python](https://www.python.org/) 
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [pandastable](https://pandastable.readthedocs.io/en/latest/examples.html) 
## Getting Started

### Prerequisites

* Python 3.10
* Windows, Linux or Mac

### Installation

#### install libraries and Dependencies 
***

* tkinter
```
pip install tk
```
* pandastable
```pip install pandastable```
* Clone the repository
```git clone https://github.com/NewcastleRSE/WorkshopScheduler.git```
### Running Locally
* run main.py
```
cd [Path to Repository]
python3.10  main.py```
### Running Tests

TBD

## Deployment

### Local

TBD

### Production

TBD
## Usage

TBD

## Roadmap

- [x] Initial Research  
- [ ] Minimum viable product <-- You are Here  
- [ ] Alpha Release  
- [ ] Feature-Complete Release  

## Contributing

### gh-pages Branch

https://newcastlerse.github.io/WorkshopScheduler/index

### Main Branch
Protected and can only be pushed to via pull requests. Should be considered stable and a representation of production code.

### Dev Branch
Should be considered fragile, code should compile and run but features may be prone to errors.

### Feature Branches
A branch per feature being worked on.

https://nvie.com/posts/a-successful-git-branching-model/

## License

## Citiation

Please cite the associated papers for this work if you use this code:

```
@article{xxx2021paper,
  title={Title},
  author={Author},
  journal={arXiv},
  year={2021}
}
```


## Acknowledgements
- This work was funded by internship funding provided by The Research Software Engineering Team of Newcastle University  
- The theme used for these GitHub Pages are based on [The Documentations Theme for Jekyll](https://jekyllthemes.io/theme/documentation)
  - https://github.com/tomjoht/documentation-theme-jekyll
