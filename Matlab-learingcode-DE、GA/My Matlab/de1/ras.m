function s = ras(pop)
%"Rastrigin" function.
%   Copyright 2003-2004 The MathWorks, Inc.
    % pop = max(-5.12,min(5.12,pop));
    s=10*size(pop,2)+sum(pop.^2 -10*cos(2*pi.*pop),2);
end