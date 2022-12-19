# Automation test website [moodle](https://moodle.org/)

## Prequisites

Already installed Docker + Docker Engine

## 📦 Installation

```
git clone https://github.com/CaoHoangKiet222/Software-Testing-Project3/
chmod +x install.sh && ./install.sh
```

## 🚀 Usage

1. Run and wait 3 minutes till the moodle installation finished.

2. Check the installation status with

```sh
docker container logs moodle
```

3. Go to `src` folder and run the following commands

> Test add assignment for admin

```sh
python3 run.py test AddAssignmentSuite
```

Create testcase by changing value in files `AddAssignmentSuite.py`
