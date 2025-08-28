
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
sorted_countries = sorted(medals, key= lambda k: medals[k], reverse=True)

top_three = sorted_countries[:3]
print(top_three)



