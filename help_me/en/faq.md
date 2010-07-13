### What is dupeGuru Music Edition?

dupeGuru Music Edition is a tool to find duplicate songs in your music collection. It can base its scan on filenames, tags or content. The filename and tag scans feature a fuzzy matching algorithm that can find duplicate filenames or tags even when they are not exactly the same.

### What makes it better than other duplicate scanners?

The scanning engine is extremely flexible. You can tweak it to really get the kind of results you want. You can read more about dupeGuru tweaking option at the [Preferences page](preferences.htm).

### How safe is it to use dupeGuru ME?

Very safe. dupeGuru has been designed to make sure you don't delete files you didn't mean to delete. First, there is the reference directory system that lets you define directories where you absolutely **don't** want dupeGuru to let you delete files there, and then there is the group reference system that makes sure that you will **always** keep at least one member of the duplicate group.

### What are the demo limitations of dupeGuru ME?

In demo mode, you can only perform actions (delete/copy/move) on 10 duplicates per session.

### The mark box of a file I want to delete is disabled. What must I do?

You cannot mark the reference (The first file) of a duplicate group. However, what you can do is to promote a duplicate file to reference. Thus, if a file you want to mark is reference, select a duplicate file in the group that you want to promote to reference, and click on **Actions-->Make Selected Reference**. If the reference file is from a reference directory (filename written in blue letters), you cannot remove it from the reference position.

### I have a directory from which I really don't want to delete files.

If you want to be sure that dupeGuru will never delete file from a particular directory, just open the **Directories panel**, select that directory, and set its state to **Reference**.

### What is this '(X discarded)' notice in the status bar?

In some cases, some matches are not included in the final results for security reasons. Let me use an example. We have 3 file: A, B and C. We scan them using a low filter hardness. The scanner determines that A matches with B, A matches with C, but B does **not** match with C. Here, dupeGuru has kind of a problem. It cannot create a duplicate group with A, B and C in it because not all files in the group would match together. It could create 2 groups: one A-B group and then one A-C group, but it will not, for security reasons. Lets think about it: If B doesn't match with C, it probably means that either B, C or both are not actually duplicates. If there would be 2 groups (A-B and A-C), you would end up delete both B and C. And if one of them is not a duplicate, that is really not what you want to do, right? So what dupeGuru does in a case like this is to discard the A-C match (and adds a notice in the status bar). Thus, if you delete B and re-run a scan, you will have a A-C match in your next results.

### I want to mark all files from a specific directory. What can I do?

Enable the [Power Marker](power_marker.htm) mode and click on the Directory column to sort your duplicates by Directory. It will then be easy for you to select all duplicates from the same directory, and then press Space to mark all selected duplicates.

### I want to remove all songs that are more than 3 seconds away from their reference file. What can I do?

* Enable the [Power Marker](power_marker.htm) mode.
* Enable the **Delta Values** mode.
* Click on the "Time" column to sort the results by time.
* Select all duplicates below -00:03.
* Click on **Remove Selected from Results**.
* Select all duplicates over 00:03.
* Click on **Remove Selected from Results**.

### I want to make my highest bitrate songs reference files. What can I do?

* Enable the [Power Marker](power_marker.htm) mode.
* Enable the **Delta Values** mode.
* Click on the "Bitrate" column to sort the results by bitrate.
* Click on the "Bitrate" column again to reverse the sort order (see Power Marker page to know why).
* Select all duplicates over 0.
* Click on **Make Selected Reference**.

### I don't want [live] and [remix] versions of my songs counted as duplicates. How do I do that?

If your comparison threshold is low enough, you will probably end up with live and remix versions of your songs in your results. There's nothing you can do to prevent that, but there's something you can do to easily remove them from your results after the scan: post-scan filtering. If, for example, you want to remove every song with anything inside square brackets []:

* **Windows**: Click on **Actions --> Apply Filter**, then type "[*]", then click OK.
* **Mac OS X**: Type "[*]" in the "Filter" field in the toolbar.
* Click on **Mark --> Mark All**.
* Click on **Actions --> Remove Selected from Results**.

### I tried to send my duplicates to Trash, but dupeGuru is telling me it can't do it. Why? What can I do?

Most of the time, the reason why dupeGuru can't send files to Trash is because of file permissions. You need *write* permissions on files you want to send to Trash. If you're not familiar with the command line, you can use utilities such as [BatChmod](http://macchampion.com/arbysoft/BatchMod) to fix your permissions.

If dupeGuru still gives you troubles after fixing your permissions, there have been some cases where using "Move Marked to..." as a workaround did the trick. So instead of sending your files to Trash, you send them to a temporary folder with the "Move Marked to..." action, and then you delete that temporary folder manually.

If all of this fail, [contact HS support](http://www.hardcoded.net/support), we'll figure it out.