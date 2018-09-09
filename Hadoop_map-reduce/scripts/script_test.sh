hadoop fs -rm -r /user/chaikesh/temp1
hadoop fs -rm -r /user/chaikesh/merged
hadoop fs -rm -r /user/chaikesh/indexwise
hadoop fs -rm -r /user/chaikesh/prediction

hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D stream.map.output.field.separator='\t'  -D stream.num.map.output.key.fields=2 -D mapred.text.key.partitioner.options=-k1,2 -files /home/chaikesh/turing/mapper_test.py,/home/chaikesh/turing/wordReducer.py -mapper /home/chaikesh/turing/mapper_test.py -reducer /home/chaikesh/turing/wordReducer.py -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -jobconf mapred.map.tasks=1 -jobconf mapred.reduce.tasks=1 -input /user/chaikesh/test -output /user/chaikesh/temp1



hadoop fs -get /user/chaikesh/counts/* /home/chaikesh/turing/counts
hadoop fs -get /user/chaikesh/temp1/* /home/chaikesh/turing/temp1
cat /home/chaikesh/turing/counts/* /home/chaikesh/turing/temp1/* >> /home/chaikesh/turing/merged.txt
hadoop fs -mkdir /user/chaikesh/merged
hadoop fs -put /home/chaikesh/turing/merged.txt /user/chaikesh/merged




hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D stream.map.output.field.separator='\t' -D stream.num.map.output.key.fields=2 -D mapred.text.key.partitioner.options=-k1,1  -files /home/chaikesh/turing/mapper2.py,/home/chaikesh/turing/reducer2.py -mapper /home/chaikesh/turing/mapper2.py -reducer /home/chaikesh/turing/reducer2.py -cacheFile /user/chaikesh/counts/part-00000#train_dict -jobconf mapred.reduce.tasks=1 -input /user/chaikesh/merged -output /user/chaikesh/indexwise

hadoop fs -get /user/chaikesh/indexwise/* /home/chaikesh/turing/indexwise

cat /home/chaikesh/turing/indexwise/* >/home/chaikesh/turing/indexwise/indexwise_merged.txt

sort -n -k 1,1 /home/chaikesh/turing/indexwise/indexwise_merged.txt > /home/chaikesh/turing/indexwise/indexwise_merged_sorted.txt 

hadoop fs -put /home/chaikesh/turing/indexwise/indexwise_merged_sorted.txt /user/chaikesh/indexwise


hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -D stream.map.output.field.separator='\t' -D stream.num.map.output.key.fields=1 -D mapred.text.key.partitioner.options=-k1,1  -files /home/chaikesh/turing/mapper3.py,/home/chaikesh/turing/reducer3_m.py -mapper /home/chaikesh/turing/mapper3.py -reducer /home/chaikesh/turing/reducer3_m.py  -cacheFile /user/chaikesh/counts/part-00000#train_dict -jobconf mapred.reduce.tasks=1 -input /user/chaikesh/indexwise/indexwise_merged_sorted.txt -output /user/chaikesh/prediction

hadoop fs -get /user/chaikesh/prediction/* /home/chaikesh/turing/prediction

cat /home/chaikesh/turing/prediction/* >/home/chaikesh/turing/prediction/prediction_merged.txt

sort -n -k 1,1 /home/chaikesh/turing/prediction/prediction_merged.txt > /home/chaikesh/turing/prediction/prediction_merged_sorted.txt 







