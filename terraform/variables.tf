variable "filename" {
  default     = "${path.module}/pets.txt"
}
variable "content" {
  default     = "We love pets!"
}
variable "prefix" {
  default     = "Mrs"
}
variable "separator" {
  default     = "."
}
variable "length" {
  default     = "1"
}



# variable "prefix {
#   default     = {
#     "statement1" = "We love pets!"
#     "statement2" = "We love animals!"
#   }
#   type = map
# }

# variable "prefix {
#   default     = ["Mr", "Mrs", "Sir"]
#   type = list
# }
