#pyramid triangle with stars
  #               * 
  #             * * *
  #           * * * * *
  #         * * * * * * *
  #       * * * * * * * * *
  #     * * * * * * * * * * *
  #   * * * * * * * * * * * * *
  # * * * * * * * * * * * * * * *

n=10
for x in range(1,n):
  for i in range(n-x):
    print(" ",end=" ")
  for y in range(1,x):
    print("*",end=" ")
  for y in range(2,x):
    print("*",end=" ")
  print()

#reverse pyramid triangel
#  * * * * * * * * * * * * * * * * *
#     * * * * * * * * * * * * * * *
#       * * * * * * * * * * * * *
#         * * * * * * * * * * *
#           * * * * * * * * *
#             * * * * * * *
#               * * * * *
#                 * * *
#                   *

n=10
for x in range(1,n):
  for i in range(x):
    print(" ",end=" ")
  for y in range(n-x):
    print("*",end=" ")
  for y in range(n-1-x):
    print("*",end=" ")
  print()