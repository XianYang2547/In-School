function y=Schaffer(x)

[row,col]=size(x);
if row>1
    error('输入的参数错误');
end
y1=x(1,1);
y2=x(1,2);
temp=y1^2+y2^2;
y=0.5-(sin(sqrt(temp))^2-0.5)/(1+0.001*temp)^2;
y=-y;
