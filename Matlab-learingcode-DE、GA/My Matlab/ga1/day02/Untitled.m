clc;%线性约束
fun = @fitnessfun; % 设置适应度函数句柄
nvars = 3; % 自变量个数
A = [-10,-20,-1;1,2,4];  b = [-100;40];  % A·x <= b约束
Aeq = [9,6,1];  beq = [100];             % Aeq·x = beq约束
lb = [2;2;2];  ub = [10;10;10];          % 定义域lb <= x <= ub
[x_best, fval] = ga(fun, nvars, A,b,Aeq,beq,lb,ub,[],[]);%未设置参数，使用默认值
function z = fitnessfun(x)
    z = (x(2)-x(1).^2).^2 + (1-x(1)).^2 + (x(3) - x(2).^2).^2 + (1 - x(2)).^2;
end