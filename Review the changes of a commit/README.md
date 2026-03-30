# ¿What is in this thing?

When I was a child it always amazed me that adults just seemed to know where things went.

> Child-Iven: I need some string. Do we have any?<br>
> Adult: In the junk drawer. There's some in there.

That wasn't usually the extent of the conversation. Something along the lines continued.

> Child-Iven: How do you know?<br>
> Adult: Experience and habit. And that's where it goes.<br>
> Child-Iven: Why does it go there?<br>
> Adult: That's where we put it. If you need something thicker we have rope in the garage.<br>
> Child-Iven: But how would I know there's string in there?<br>
> Adult: You ask me.<br>
> Child-Iven: What if I need some and I can't ask you?<br>
> Adult: Well now you know so you don't need to ask anymore.

Most adults want the top interaction. Question. Answer. Done. The child moves on. If not, what follows sometimes feels like it lasts longer than Christmas at the in-laws... The end can't come fast enough. You get an endless loop.

```
1: Question
2: Answer
3: Goto 1
```

The root of these questions is a lack of labels. The container doesn't indicate what it contains.

## ¿What does this have to do with git?

Review commit "containers" with `git log --oneline` to see the high level commit messages. With good commit messages you'll know what it contains.

```git
ivenbach MINGW64 /e/repos/Learning-to-understand-git (showCommitsPatch)
$ git log --oneline
593c013 (HEAD -> showCommitsPatch, origin/main, origin/HEAD, main) Merge branch 'READMEdiffCheck'
a778dc0 Commit to preview diff check
c6f5ebb Add guard clause for zero denominator
e11cddd Add mathematical methods
f847e91 Adding parts of a file - Start of file update
961d82a Add specific parts of files README
...
ivenbach MINGW64 /e/repos/Learning-to-understand-git (showCommitsPatch)
$
```

When you find a commit you want to investigate, execute `git show [-p | -u | --patch] <commit-hash>`. You will be shown a diff that applied the changes. From there you can review the commit to find what you need. If not, you can review another commit's patch.

```git
ivenbach MINGW64 /e/repos/Learning-to-understand-git (showCommitsPatch)
$ git show -p c6f5ebb
...
    Add guard clause for zero denominator

diff --git a/Adding specific parts of files/adding_specific_parts_of_a_file.py b/Adding specific parts of files/adding_specific_parts_of_a_file.py
index a1f8419..46b15a3 100644
--- a/Adding specific parts of files/adding_specific_parts_of_a_file.py
+++ b/Adding specific parts of files/adding_specific_parts_of_a_file.py
@@ -10,6 +10,8 @@ def multiplying_two_numbers(multiplier, multiplicand):
     return multiplier * multiplicand

 def dividing_two_numbers(numerator, denominator):
+    if denominator == 0:
+        raise ValueError("Denominator cannot be zero.")
     return numerator / denominator

 # Plenty of code in between
```
