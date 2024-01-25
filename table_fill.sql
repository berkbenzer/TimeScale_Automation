DO $$ 
DECLARE
    StartDate TIMESTAMP WITH TIME ZONE := NOW() - INTERVAL '1220 days';
    EndDate TIMESTAMP WITH TIME ZONE := NOW();
    Counter INT := 1;
BEGIN
    WHILE StartDate <= EndDate LOOP
        INSERT INTO public.conditions_1 ("time", location, temperature, humidity)
        VALUES (
            StartDate,
            'Location' || Counter,
            RANDOM() * 30 + 100,  -- Random temperature between 20 and 50
            RANDOM() * 30 + 140   -- Random humidity between 40 and 70
        );

        StartDate := StartDate + INTERVAL '1 hour';
        Counter := Counter + 1;
    END LOOP;
END $$;