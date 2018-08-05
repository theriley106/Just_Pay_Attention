Just_Pay_Attention
===============

Employee compliance training videos often have a component that pauses the training when the window is not in focus.

Javascript example:

```javascript
window.addEventListener('focus', function() {
  document.querySelector('video').play();
});

window.addEventListener('blur', function() {
  document.querySelector('video').pause();
});
```

This is implemented into the compliance training videos to *ensure* that the employee is actively participating.  It intentionally limits multitasking requiring the employee to only focus on the one task.  Unfortunately this is something that's relatively easy to bypass by opening up the compliance training in a VM or simply leaving your desk while the training completes.

To ensure 100% employee attentiveness, I've created a framework that uses brain waves from a commercial EEG headset as well as pupil/eye tracking using OpenCV to quantify how attentive an employee is.  If the program detects that the employee is no longer paying attention the video will pause.  Positively ensuring that the content is absorbed in it's entirety.

I thought it would be interesting to branch off of this concept, and create a way of
