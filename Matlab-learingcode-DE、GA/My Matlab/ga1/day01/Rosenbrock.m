function f=Rosenbrock(x)
% n = size(p,2);
%x = sym('x',[n,1]);
n=10;

f = sum(100*(x(2:2:n)-x(1:2:n).^2).^2 + (1-x(1:2:n)).^2);

