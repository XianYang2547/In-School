clear;%非线性约束
clc
options = gaoptimset('PopulationSize',200, 'Generations', 600); % 遗传算法相关配置
fun = @fitnessfun; % 设置适应度函数句柄
nonlcon = @nonlconfun; % 设置非线性约束函数句柄
nvars = 3; % 自变量个数
A = [];  b = [];
Aeq = [];  beq = [];
lb = [0;0;0];  ub = [];
[x_best, fval] = ga(fun, nvars, A,b,Aeq,beq,lb,ub,nonlcon,options);
 
function [c,ceq] = nonlconfun(x)
    c(1,1) = -x(1)^2 + x(2) - x(3)^3;
    c(2,1) = x(1) + x(2)^2 + x(3)^3 - 20;
    ceq(1,1) = -x(1) - x(2)^2 + 2;
    ceq(2,1) = x(2) + 2*x(3) - 3;
end
 
function f = fitnessfun(x)
    f = x(1)^2 + x(2)^2 + x(3)^3 + 8;
end