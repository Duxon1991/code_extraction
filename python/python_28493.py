# Array of str objects into a single int array in python
&gt;&gt;&gt; [t for j in [map(int,i.strip('[]').split()) for i in arr] for t in j]
[74, 73, 74, 74, 73, 73, 73, 74, 74, 73, 74, 73, 147, 74, 73, 74, 73, 74, 147, 74, 73, 73, 74, 73, 74, 74, 73, 73, 73, 74, 73, 147, 74, 74, 73, 147, 74, 73, 73, 74, 73, 74, 74, 73, 73, 73, 74, 73, 74, 73, 74, 73, 73, 74, 73, 74, 74, 73, 73, 74]
