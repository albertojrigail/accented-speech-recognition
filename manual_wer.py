from jiwer import wer

ground_truth = "Please call Stella.  Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob.  We also need a small plastic snake and a big toy frog for the kids.  She can scoop these things into three red bags, and we will go meet her Wednesday at the train station."
hypothesis = "please go teacher to green this things with her from the store successor presses no peace five thick as laughable cheese and may be antichamber but we also need a small plastic snakebite frock for the key she can excepting into the red backs and quilleash and the train station"
score = wer(ground_truth, hypothesis)
print(score)