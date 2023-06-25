# analysis_of_annual_salary

## 작업

<br />
- 대학 전공별 졸업 후의 연봉 데이터 웹 크롤링 및 데이터 분석
- 분석한 데이터를 내보내기 위해 Flask 서버 구축
  - 구축한 서버 API 종류

1. 전체 데이터

2. 각 컬럼별 데이터

3. 각 컬럼별 내림차순 데이터

4. 전체 데이터에서 선택한 컬럼 내림차순 오름차순

<br />
<br />

## API

- 전체 데이터
  - `/r_sal_maj`

```json
[
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 93200,
    "High Meaning %": 67.0,
    "Major": "Petroleum Engineering",
    "Mid-Career Pay": 187300,
    "Unnamed: 0": 0,
    "id": 1
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 84800,
    "High Meaning %": 28.0,
    "Major": "Operations Research & Industrial Engineering",
    "Mid-Career Pay": 170400,
    "Unnamed: 0": 1,
    "id": 2
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 108500,
    "High Meaning %": 46.0,
    "Major": "Electrical Engineering & Computer Science (EECS)",
    "Mid-Career Pay": 159300,
    "Unnamed: 0": 2,
    "id": 3
  }
  ...
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36900,
    "High Meaning %": 0.0,
    "Major": "Mental Health",
    "Mid-Career Pay": 45000,
    "Unnamed: 0": 824,
    "id": 825
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36000,
    "High Meaning %": 0.0,
    "Major": "Medical Assisting",
    "Mid-Career Pay": 44800,
    "Unnamed: 0": 825,
    "id": 826
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 40000,
    "High Meaning %": 33.0,
    "Major": "Metalsmithing",
    "Mid-Career Pay": 40300,
    "Unnamed: 0": 826,
    "id": 827
  }
]
```

<br />

- max 데이터
  - `/r_sal_maj/ear_career_pay/max`
  - `/r_sal_maj/mid_career_pay/max`
  - `/r_sal_maj/high_meaning/max`

```json
{
  "Degree Type": "Bachelors",
  "Early Career Pay": 108500,
  "High Meaning %": 46.0,
  "Major": "Electrical Engineering & Computer Science (EECS)",
  "Mid-Career Pay": 159300,
  "Unnamed: 0": 2,
  "id": 3
}
```

<br />

- min 데이터
  - `/r_sal_maj/ear_career_pay/min`
  - `/r_sal_maj/mid_career_pay/min`
  - `/r_sal_maj/high_meaning/min`

```json
{
  "Degree Type": "Bachelors",
  "Early Career Pay": 34500,
  "High Meaning %": 57.0,
  "Major": "Voice & Opera",
  "Mid-Career Pay": 53300,
  "Unnamed: 0": 804,
  "id": 805
}
```

<br />

- Mid-Career Pay 컬럼 데이터 & 내림차순
  - `/r_sal_maj/mid_career_pay_all`
  - `/r_sal_maj/mid_career_pay_all/ascending`

```json
/r_sal_maj/mid_career_pay_all

[
  {
    "Mid-Career Pay": 187300,
    "id": 1
  },
  {
    "Mid-Career Pay": 170400,
    "id": 2
  }
  ...
  {
    "Mid-Career Pay": 44800,
    "id": 826
  },
  {
    "Mid-Career Pay": 40300,
    "id": 827
  }
]

/r_sal_maj/mid_career_pay_all/ascending

[
  {
    "Mid-Career Pay": 40300,
    "id": 827
  },
  {
    "Mid-Career Pay": 44800,
    "id": 826
  }
  ...
   {
    "Mid-Career Pay": 170400,
    "id": 2
  },
  {
    "Mid-Career Pay": 187300,
    "id": 1
  }
]

```

<br />

- Early Career Pay 컬럼 데이터 & 내림차순
  - `/r_sal_maj/ear_career_pay_all`
  - `/r_sal_maj/ear_career_pay_all/ascending`

```json
/r_sal_maj/ear_career_pay_all

[
  {
    "Early Career Pay": 93200,
    "id": 1
  },
  {
    "Early Career Pay": 84800,
    "id": 2
  }
  ...
  {
    "Early Career Pay": 36000,
    "id": 826
  },
  {
    "Early Career Pay": 40000,
    "id": 827
  }
]

/r_sal_maj/ear_career_pay_all/ascending

[
  {
    "Early Career Pay": 34500,
    "id": 805
  },
  {
    "Early Career Pay": 34700,
    "id": 591
  }
  ...
  {
    "Early Career Pay": 95900,
    "id": 76
  },
  {
    "Early Career Pay": 108500,
    "id": 3
  }
]

```

<br />

- Major 컬럼 데이터
  - `/r_sal_maj/major_all`

```json
[
  {
    "Major": "Petroleum Engineering",
    "id": 1
  },
  {
    "Major": "Operations Research & Industrial Engineering",
    "id": 2
  }
  ...
  {
    "Major": "Medical Assisting",
    "id": 826
  },
  {
    "Major": "Metalsmithing",
    "id": 827
  }
]
```

<br />

- High Meaning % 컬럼 데이터 & 내림차순
  - `/r_sal_maj/high_meaning_all`
  - `/r_sal_maj/high_meaning_all/ascending`

```json
/r_sal_maj/high_meaning_all

[
  {
    "High Meaning %": 67.0,
    "id": 1
  },
  {
    "High Meaning %": 28.0,
    "id": 2
  }
  ...
  {
    "High Meaning %": 0.0,
    "id": 826
  },
  {
    "High Meaning %": 33.0,
    "id": 827
  }
]

/r_sal_maj/high_meaning_all/ascending

[
  {
    "High Meaning %": 21.0,
    "id": 102
  },
  {
    "High Meaning %": 22.0,
    "id": 190
  }
  ...
  {
    "High Meaning %": 0.0,
    "id": 825
  },
  {
    "High Meaning %": 0.0,
    "id": 826
  }
]
```

<br />

- Mid carrer Pay 컬럼이 내림차순 오름차순인 전체 데이터 : page당 10개 데이터
  - `/r_sal_maj/mid_career_pay_ascending/<int:page>`
  - `/r_sal_maj/mid_career_pay_ascending/<int:page>`

```json
[
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36100,
    "High Meaning %": 78.0,
    "Major": "Mental Health Counseling",
    "Mid-Career Pay": 50000,
    "Unnamed: 0": 816,
    "id": 817
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 41200,
    "High Meaning %": 73.0,
    "Major": "Middle School Education",
    "Mid-Career Pay": 50800,
    "Unnamed: 0": 815,
    "id": 816
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36900,
    "High Meaning %": 0.0,
    "Major": "Educational Psychology",
    "Mid-Career Pay": 51200,
    "Unnamed: 0": 814,
    "id": 815
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 37400,
    "High Meaning %": 73.0,
    "Major": "Child Development",
    "Mid-Career Pay": 51400,
    "Unnamed: 0": 813,
    "id": 814
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 38400,
    "High Meaning %": 84.0,
    "Major": "Recreational Therapy",
    "Mid-Career Pay": 51600,
    "Unnamed: 0": 812,
    "id": 813
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 39900,
    "High Meaning %": 78.0,
    "Major": "Counseling",
    "Mid-Career Pay": 51700,
    "Unnamed: 0": 811,
    "id": 812
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 38700,
    "High Meaning %": 71.0,
    "Major": "Human Services (HS)",
    "Mid-Career Pay": 52500,
    "Unnamed: 0": 810,
    "id": 811
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 38800,
    "High Meaning %": 0.0,
    "Major": "Hospitality & The Culinary Arts",
    "Mid-Career Pay": 52900,
    "Unnamed: 0": 809,
    "id": 810
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 37500,
    "High Meaning %": 44.0,
    "Major": "Baking & Pastry Arts",
    "Mid-Career Pay": 53000,
    "Unnamed: 0": 807,
    "id": 808
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 45600,
    "High Meaning %": 0.0,
    "Major": "Human Services Management",
    "Mid-Career Pay": 53000,
    "Unnamed: 0": 808,
    "id": 808
  }
]
```

<br />

- early career pay 컬럼이 내림차순, 오름차순인 전체 데이터 : page당 10개 데이터
  - `/r_sal_maj/ear_career_pay_ascending/<int:page>`
  - `/r_sal_maj/ear_career_pay_deascending/<int:page>`

```json
// ascending

[
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 40000,
    "High Meaning %": 33.0,
    "Major": "Metalsmithing",
    "Mid-Career Pay": 40300,
    "Unnamed: 0": 826,
    "id": 827
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36000,
    "High Meaning %": 0.0,
    "Major": "Medical Assisting",
    "Mid-Career Pay": 44800,
    "Unnamed: 0": 825,
    "id": 826
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36900,
    "High Meaning %": 0.0,
    "Major": "Mental Health",
    "Mid-Career Pay": 45000,
    "Unnamed: 0": 824,
    "id": 825
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36100,
    "High Meaning %": 78.0,
    "Major": "Early Childhood Education",
    "Mid-Career Pay": 45400,
    "Unnamed: 0": 823,
    "id": 824
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 37400,
    "High Meaning %": 52.0,
    "Major": "Outdoor Education",
    "Mid-Career Pay": 46300,
    "Unnamed: 0": 822,
    "id": 823
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 39200,
    "High Meaning %": 0.0,
    "Major": "Rehabilitation Counseling",
    "Mid-Career Pay": 46400,
    "Unnamed: 0": 821,
    "id": 822
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36400,
    "High Meaning %": 73.0,
    "Major": "Child & Family Studies",
    "Mid-Career Pay": 46500,
    "Unnamed: 0": 820,
    "id": 821
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 38000,
    "High Meaning %": 84.0,
    "Major": "Addiction Studies",
    "Mid-Career Pay": 47000,
    "Unnamed: 0": 819,
    "id": 820
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 35700,
    "High Meaning %": 50.0,
    "Major": "Equine Studies",
    "Mid-Career Pay": 47100,
    "Unnamed: 0": 818,
    "id": 819
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 38000,
    "High Meaning %": 77.0,
    "Major": "Early Childhood & Elementary Education",
    "Mid-Career Pay": 48400,
    "Unnamed: 0": 817,
    "id": 818
  }
]

// deascending

[
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 34500,
    "High Meaning %": 57.0,
    "Major": "Voice & Opera",
    "Mid-Career Pay": 53300,
    "Unnamed: 0": 804,
    "id": 805
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 34700,
    "High Meaning %": 41.0,
    "Major": "Painting & Printmaking",
    "Mid-Career Pay": 73600,
    "Unnamed: 0": 593,
    "id": 591
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 35600,
    "High Meaning %": 0.0,
    "Major": "Psychology & Human Services",
    "Mid-Career Pay": 59400,
    "Unnamed: 0": 764,
    "id": 764
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 35700,
    "High Meaning %": 50.0,
    "Major": "Equine Studies",
    "Mid-Career Pay": 47100,
    "Unnamed: 0": 818,
    "id": 819
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 35800,
    "High Meaning %": 79.0,
    "Major": "Rehabilitation Services",
    "Mid-Career Pay": 60200,
    "Unnamed: 0": 756,
    "id": 757
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36000,
    "High Meaning %": 0.0,
    "Major": "Medical Assisting",
    "Mid-Career Pay": 44800,
    "Unnamed: 0": 825,
    "id": 826
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36100,
    "High Meaning %": 78.0,
    "Major": "Mental Health Counseling",
    "Mid-Career Pay": 50000,
    "Unnamed: 0": 816,
    "id": 817
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36100,
    "High Meaning %": 78.0,
    "Major": "Early Childhood Education",
    "Mid-Career Pay": 45400,
    "Unnamed: 0": 823,
    "id": 824
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36400,
    "High Meaning %": 76.0,
    "Major": "Biblical Studies & Practical Ministries",
    "Mid-Career Pay": 58900,
    "Unnamed: 0": 767,
    "id": 768
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 36400,
    "High Meaning %": 73.0,
    "Major": "Child & Family Studies",
    "Mid-Career Pay": 46500,
    "Unnamed: 0": 820,
    "id": 821
  }
]
```

<br />

- high meaning 컬럼이 내림차순, 오름차순인 전체 데이터
  - `/r_sal_maj/high_meaning_ascending/<int:page>`
  - `/r_sal_maj/high_meaning_descending/<int:page>`

```json
// ascending

[
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 51500,
    "High Meaning %": 21.0,
    "Major": "Japanese Studies",
    "Mid-Career Pay": 113800,
    "Unnamed: 0": 102,
    "id": 102
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 59000,
    "High Meaning %": 22.0,
    "Major": "International Marketing",
    "Mid-Career Pay": 102600,
    "Unnamed: 0": 189,
    "id": 190
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 43800,
    "High Meaning %": 23.0,
    "Major": "Commercial Photography",
    "Mid-Career Pay": 71300,
    "Unnamed: 0": 634,
    "id": 634
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 56300,
    "High Meaning %": 24.0,
    "Major": "Food Marketing",
    "Mid-Career Pay": 102700,
    "Unnamed: 0": 188,
    "id": 188
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 49900,
    "High Meaning %": 25.0,
    "Major": "Web Design",
    "Mid-Career Pay": 69800,
    "Unnamed: 0": 653,
    "id": 653
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 54800,
    "High Meaning %": 27.0,
    "Major": "International Trade & Business",
    "Mid-Career Pay": 86800,
    "Unnamed: 0": 378,
    "id": 379
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 47500,
    "High Meaning %": 27.0,
    "Major": "Fashion Design",
    "Mid-Career Pay": 87700,
    "Unnamed: 0": 370,
    "id": 371
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 81100,
    "High Meaning %": 28.0,
    "Major": "Computer Science (CS) & Business",
    "Mid-Career Pay": 94600,
    "Unnamed: 0": 278,
    "id": 279
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 84800,
    "High Meaning %": 28.0,
    "Major": "Operations Research & Industrial Engineering",
    "Mid-Career Pay": 170400,
    "Unnamed: 0": 1,
    "id": 2
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 52700,
    "High Meaning %": 28.0,
    "Major": "Advertising Design",
    "Mid-Career Pay": 91300,
    "Unnamed: 0": 327,
    "id": 328
  }
]

// deascending

[
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 43100,
    "High Meaning %": 93.0,
    "Major": "Music Therapy",
    "Mid-Career Pay": 60700,
    "Unnamed: 0": 754,
    "id": 755
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 60600,
    "High Meaning %": 92.0,
    "Major": "Medicine",
    "Mid-Career Pay": 109200,
    "Unnamed: 0": 129,
    "id": 130
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 68400,
    "High Meaning %": 90.0,
    "Major": "Radiation Therapy",
    "Mid-Career Pay": 93400,
    "Unnamed: 0": 295,
    "id": 296
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 48900,
    "High Meaning %": 90.0,
    "Major": "Cardiopulmonary Science",
    "Mid-Career Pay": 73400,
    "Unnamed: 0": 594,
    "id": 595
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 61900,
    "High Meaning %": 89.0,
    "Major": "Cytotechnology",
    "Mid-Career Pay": 78200,
    "Unnamed: 0": 520,
    "id": 521
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 55500,
    "High Meaning %": 88.0,
    "Major": "Physical Therapy",
    "Mid-Career Pay": 98200,
    "Unnamed: 0": 238,
    "id": 237
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 54100,
    "High Meaning %": 88.0,
    "Major": "Occupational Therapy (OT)",
    "Mid-Career Pay": 93300,
    "Unnamed: 0": 297,
    "id": 297
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 43100,
    "High Meaning %": 87.0,
    "Major": "American Sign Language Interpreting",
    "Mid-Career Pay": 78300,
    "Unnamed: 0": 517,
    "id": 518
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 64300,
    "High Meaning %": 86.0,
    "Major": "Diagnostic Medical Sonography",
    "Mid-Career Pay": 81400,
    "Unnamed: 0": 471,
    "id": 472
  },
  {
    "Degree Type": "Bachelors",
    "Early Career Pay": 43500,
    "High Meaning %": 85.0,
    "Major": "Mortuary Science",
    "Mid-Career Pay": 64000,
    "Unnamed: 0": 726,
    "id": 725
  }
]
```
