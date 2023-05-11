# oscilloscope
This oscilliscope uses artifical intelligence to more accurately measure the fundamental frequnciy of a sound wave based in the enviorment of Providence Rhode Island on a fine Spring day. 
## Motivations
As we were measuring the frequncies of tuning forks with electronic software, we found there to be a disparity between the frequency number on the tuning fork versus that of the computer. Hence, we deduced that somewhere in the middle would be the true frequency (since the computer was reading much too high), but the computer's microphone was not sensitive enough to read the true value.
We believe an neural net applying multilinear regression would be able to fill in the gap to more accurealy meaure which frequncy the tuning fork is produced. by standardizing it's output values based on the input of multiple different, procured sounds - either tuning forks or perfect sin waves (from another computer). This is our basis for the neural network.

## How it works
For each sound wave in the training set, there is an "expected" output. This is compared against what the computer naturally outputs as it's value for the same input sound wave. The difference in these values is minimized across every soundwave in the data set to develop the neural network as it's trained. IN this way, a feedback loop is created that fills in the gap between the frequency on the tuning fork and that of what the computer reads. 
Then, the nueral network is able to predict a possible fundamental frequency for 

## Future work
Since training it specfiic to it's enviornment, the program should include some self-training component inside of it, where the computer outputs and reads sinwaves to train it's neural net for other use (tuning instrumetns, frequency correction, etc.). Also, the trained NN is specific to the range of the tuning forks, for specific use in it's context of physics 560. I restricted any output outside of the tuning fork's range, since it was generally off due to extrapolation considerations. Incorporating a more broad range into this "self-training" routine in the program could signifcantly increase the versatility of it.
