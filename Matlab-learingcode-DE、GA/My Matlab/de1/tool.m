clc;
clear;
options=gaoptimset('PopulationSize',100,'CrossoverFraction',0.8,'Generations',1000,'MigrationFraction',0.1);% 设置种群大小100，交叉概率0.8，迭代300次,变异概率0.1
%% ga函数的参数设置
fun = @pj; % 设置适应度函数句柄，在定义的函数名前加个@即可
nvars = 10; % 自变量个数，本题为2个自变量
A = [];  b = []; 
Aeq = [];  beq = []; % 没有约束就赋值为空矩阵
lb = [-50;-50;-50;-50;-50;-50;-50;-50;-50;-50];  ub = [50;50;50;50;50;50;50;50;50;50];  % 对自变量x的限制
%% 调用ga函数计算
% 调用格式[x_best,fval] = ga(fun,nvars,A,b,Aeq,beq,lb,ub,nonlcon,options); 
% fun是函数句柄， nvars变量数，A,b,Aeq,Beq是线性约束，lb,ub限制X范围，
% nonlcon是非线性约束，做线性规划寻优时赋值为空即可。options是设定参数的结构体
[x_best, fval] = ga(fun, nvars, A,b,Aeq,beq,lb,ub,[],options);
Bestx=x_best
Bestfval=fval

%% 求这个函数的最小值
% function z = fitnessfun(x)
% % 无论有几个自变量，入口参数都为一个x，表示自变量的矩阵
% % 在函数内用x(1)、x(2)等将每个自变量的值索引出来
% % 必须以这种格式编写，否则ga函数报错
%    z= (x(1)-1).^2+(x(2)-2).^2+(x(3)-3).^2+(x(4)-4).^2+(x(5)-5).^2;
% end
% function y = Rastrigin(x)
%     [row,~] = size(x);
%     if  row > 1 
%         error( ' 输入的参数错误 ' );
%     end
%     y = sum(x.^2 - 10 * cos( 2 * pi * x) + 10 );
% 
% end
function f=Rosenbrock(x)
% n = size(p,2);
%x = sym('x',[n,1]);
n=10;

f = sum(100*(x(2:2:n)-x(1:2:n).^2).^2 + (1-x(1:2:n)).^2);
end