
hadoop fs -rm -r /user/chaikesh/counts



hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D stream.map.output.field.separator='\t'  -D stream.num.map.output.key.fields=2 -D mapred.text.key.partitioner.options=-k1,2  -files /home/chaikesh/turing/mapper_train.py,/home/chaikesh/turing/wordReducer.py -mapper /home/chaikesh/turing/mapper_train.py -reducer /home/chaikesh/turing/wordReducer.py -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner  -jobconf mapred.reduce.tasks=1 -input /user/chaikesh/train  -output /user/chaikesh/counts


