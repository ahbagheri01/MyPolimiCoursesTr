# ANN2DL-20260916-Intro-DeepLearning — Additional Professor Notes

**Transcripts:** Matteo Matteucci's Personal Room-20260916 1645-1.txt
**Materials:** E:\amirhossein\Polimi\POLIMI\ANN2DL\00 - AN2DL Intro (TENTATIVE).pdf, E:\amirhossein\Polimi\POLIMI\ANN2DL\01 - DeepLearningIntro.pdf

## Recommended Study Plan and Course Sequencing

**Reference:** 00 - AN2DL Intro (TENTATIVE).pdf, slide 3-4

Professor Matteucci advises that students in their first year of the Master's (magistrale) delay this course to their second year. The intended academic path is to take Machine Learning and Uncertainty in AI during the first year, followed by Artificial Neural Networks and Deep Learning in the second year. Students with immediate scheduling conflicts with Uncertainty in AI should follow this standard sequence.

## Historical Scope and Curriculum Boundaries

**Reference:** 00 - AN2DL Intro (TENTATIVE).pdf, slide 8

The course specifically covers neural network and deep learning developments spanning from 1956 up through roughly 2016–2017. Deep learning topics from 2016–2017 to the present (including advanced transformer architectures, LLMs, and modern generative AI) are reserved for a separate second-semester course ('Advanced Deep Learning') or specialized courses like NLP.

## Challenge Evaluation Criteria and Report Expectations

**Reference:** 00 - AN2DL Intro (TENTATIVE).pdf, slide 14-17

Kaggle challenge points are not strictly assigned by leaderboard ranking. Submissions that perform below the random baseline or simply cut-and-paste lab notebooks will receive minimal credit. The evaluation heavily weights the accompanying report, which must clearly demonstrate the team's genuine struggle, personal problem-solving journey, and obstacles encountered, rather than presenting a polished, AI-generated summary.

## Oral Verification Format to Detect Generative AI Use

**Reference:** 00 - AN2DL Intro (TENTATIVE).pdf, slide 15

To counter the submission of challenge projects solved entirely by LLMs (e.g., Claude or ChatGPT), an oral interview will be conducted with randomly selected team members (only 1 member per team will be interviewed, creating a ~75% chance a given student is not tested directly). The ~10-minute interview determines the team's multiplicative factor alpha in {0, 0.25, 0.5, 0.75, 1}.

## Grading Role of the Homework Challenge

**Reference:** 00 - AN2DL Intro (TENTATIVE).pdf, slide 14

Students often believe the homework challenge exists solely to achieve top honors (30L), but Matteucci emphasizes that historically its primary practical role is helping struggling students pass the course (securing the 18/30 threshold). Because full marks are significantly harder to achieve on the theoretical written exam than on the challenge, participating fully in the challenge is essential.

## SEB Practice Quiz Exit Password and Linux Workarounds

**Reference:** 00 - AN2DL Intro (TENTATIVE).pdf, slide 18, 24

Safe Exam Browser (SEB) completely locks down the student's operating system. To safely exit the mock/test quiz provided on WeBeep, students must enter the exact password 'IAmDone'. Since SEB does not operate on Linux and virtual machines are blocked to prevent cheating, Linux users must borrow a Windows/Mac laptop or boot Windows from an external drive.

## Non-Statistical Machine Learning vs Statistics

**Reference:** 01 - DeepLearningIntro.pdf, slide 2-3

While statistical methods are foundational to machine learning, not all ML techniques derive from statistics. For example, decision trees and rule induction are fundamentally non-statistical (unlike random forests or bagging/boosting which rely heavily on statistical principles). This demonstrates that machine learning is a multidisciplinary field overlapping with statistics, AI, databases/data mining, and pattern recognition.

## Why Deep Learning Succeeded on Signals Over Hand-Crafted Pipelines

**Reference:** 01 - DeepLearningIntro.pdf, slide 24-26, 36

Deep learning is fundamentally representation learning: simultaneously optimizing feature extractors and classifiers end-to-end. It uniquely excels on raw signals (images, audio time series) because humans cannot hand-engineer rules for millions of pixel configurations (e.g., specifying every pixel pattern for glasses or pointed cat ears). Hierarchical trainable extractors build abstractions automatically from low-level edges to high-level semantic parts.
