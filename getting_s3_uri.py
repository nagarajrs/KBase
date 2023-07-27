def list_s3_batch(uri):
    '''
    lists all XML in an s3 bucket ***WARNING*** there's a TON of files. Not recommended to use this in python.
    I recommend using xarg command to stream the data so individual file URI can be used per script call.
    e.g. uri s3://alks-arda/dsc/patent_db/data/xml/2021/2021
    '''
    ans = shell_run(f"aws s3 ls {uri} ")

    #ans = shell_run(f"ls")
    for row in ans.stdout.decode().split("\n"):
      if row.strip():
        filename = row.split()[-1]
        yield f"{uri}/{filename}" 
