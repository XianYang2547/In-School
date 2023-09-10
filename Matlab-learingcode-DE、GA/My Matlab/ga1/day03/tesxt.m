clc;
clear;
fun=@fitnessfun;
nonlcon=@nonlconfun;
Aeq=[1,-2];beq=[-1];
lb=[0;0];ub=[10;10];
nvars=2;
[x_best, fval] = ga(fun, nvars, [],[],Aeq,beq,lb,ub,nonlcon,[]);
x_best
fval

function [c,ceq]=nonlconfun(x)
c=[];
ceq=(x(1)^2)/4+x(2)^2-1;
end


function y=fitnessfun(x)
y=(x(1)-2)^2+(x(2)-1)^2;
end