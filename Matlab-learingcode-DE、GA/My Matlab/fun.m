function y = fun(x,label)
%函数用于计算粒子适应度值
%x           input           输入粒子 
%y           output          粒子适应度值 
if label==1
    y=-Rastrigin(x);
elseif label==2
    y=-Schaffer(x);
else
    y=-Griewank(x);
end
