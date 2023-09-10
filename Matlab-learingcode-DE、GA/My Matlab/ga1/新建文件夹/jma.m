%定义解码 jma 的函数
function x2=jma(x1)
x2=zeros(1,5);
for j=1:5
    x3=(j-1)*7+1;
    x4=x3:(x3+6);
    x5=str2num(x1(x4))/100000;
    x2(j)=[x5-50];
end

end 