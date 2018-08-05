<h1 align="center">Just Pay Attention</h1>

<p align="center"><b>Employee compliance training that uses EEG waves and Pupil Detection to pause when the user isn't paying attention</b></p>

<h2 align="center"><a href="https://www.youtube.com/watch?v=ttMWoj_lk0o">Click Here to Watch the Demo on Youtube</a></h2>

## Overview

Most modern employee compliance training and employee onboarding videos have a component that pauses the training when the window is not in focus.

```javascript
// Javascript Example
window.addEventListener('focus', function() {
  document.querySelector('video').play();
});

window.addEventListener('blur', function() {
  document.querySelector('video').pause();
});
```

This is used to *ensure* that the employee is actively participating in the training by limiting the ability to multitask.

This concept was really interesting to me, and I was curious to see if there was an increase in information retention if the software limits an employees ability to multitask on an assignment. I thought that this concept could also be applied to a ton of different areas as well: Netflix user attentiveness, Kicking a inactive user from an online game, More accurate data about advertisement consumption, etc.

I also wanted to take it a step further and redefine the way it considers the user to be at attention.  Most compliance training frameworks only use the currently focused window to determine attentiveness, but this classification fails if the user simply opens up the window and walks away.

The *Just_Pay_Attention* framework uses a combination of brain waves from a commercial EEG headset and Pupil/Eye detection using OpenCV to quantify how attentive the user is.  In the case of compliance training, the training will pause if the program detects that the employee is no longer paying attention.

[![N|Solid](static/ui.png)](#)
<p align="center">Example Compliance Training Website</p>
